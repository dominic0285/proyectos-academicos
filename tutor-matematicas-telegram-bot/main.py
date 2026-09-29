import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
import re # Para expresiones regulares, útil para extraer el tipo de operación

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, filters
)

# Cargar variables de entorno
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configurar Gemini con la API key
genai.configure(api_key=GEMINI_API_KEY)

# Inicializar el modelo de Gemini
# Usamos 'models/gemini-1.5-flash-latest' por su velocidad y eficiencia.
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# Memoria local
MEMORY_FILE = "memory.json"
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
else:
    memory = {}

def save_memory():
    """Guarda el estado actual de la memoria en el archivo JSON."""
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

# --- Funciones de Utilidad ---

def get_user_data(user_id: str):
    """Obtiene los datos del usuario de la memoria, inicializándolos si no existen."""
    if user_id not in memory:
        memory[user_id] = {
            "state": "INITIAL", # Nuevo estado para la conversación inicial
            "name": None,
            "age": None,
            "errores": 0,
            "aciertos": 0,
            "last_error_type": None # Para recordar el tipo de operación con error
        }
    save_memory() # Guardar inmediatamente después de inicializar
    return memory[user_id]

# --- Comandos del Bot ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /start, inicializa el usuario y comienza la conversación."""
    user_id = str(update.message.from_user.id)
    user_data = get_user_data(user_id) # Asegura que los datos existan

    user_data["state"] = "ASKING_NAME"
    save_memory()

    await update.message.reply_text(
        "¡Hola! 👋 Soy tu tutor de matemáticas. Para empezar, ¿cuál es tu nombre?"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Procesa los mensajes de texto del usuario con Gemini."""
    user_input = update.message.text
    user_id = str(update.message.from_user.id)
    user_data = get_user_data(user_id) # Obtiene los datos del usuario

    # --- Lógica de la conversación inicial ---
    if user_data["state"] == "ASKING_NAME":
        user_data["name"] = user_input.strip()
        user_data["state"] = "ASKING_AGE"
        save_memory()
        await update.message.reply_text(f"¡Mucho gusto, {user_data['name']}! 😊 ¿Cuántos años tienes?")
        return

    if user_data["state"] == "ASKING_AGE":
        try:
            age = int(user_input.strip())
            if 4 <= age <= 12: # Rango de edad razonable para primaria
                user_data["age"] = age
                user_data["state"] = "READY"
                save_memory()
                keyboard = [
                    [InlineKeyboardButton("🆘 Necesito ayuda", callback_data="help")],
                    [InlineKeyboardButton("👋 Terminar", callback_data="end_chat")]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)

                await update.message.reply_text(
                    f"¡Genial, {user_data['name']} de {user_data['age']} años! 😄\n\n"
                    "Ahora, para tu tarea de matemáticas, puedes escribirme operaciones como:\n"
                    "👉 `7 x 3` (para multiplicación)\n"
                    "👉 `10 % 2` (para división)\n"
                    "👉 `5 + 8` (para suma)\n"
                    "👉 `15 - 9` (para resta)\n\n"
                    "¡Estoy listo para ayudarte! O toca un botón:",
                    reply_markup=reply_markup
                )
            else:
                await update.message.reply_text(
                    "Mmm, esa edad no parece correcta para un niño de primaria. Por favor, "
                    "ingresa tu edad en años (solo el número)."
                )
        except ValueError:
            await update.message.reply_text(
                "Eso no parece un número. Por favor, ingresa tu edad en años (solo el número)."
            )
        return

    # --- Lógica principal del bot (después de la configuración inicial) ---
    if user_data["state"] == "READY":
        user_name = user_data["name"] if user_data["name"] else "niño(a)"

        prompt = f"""
Actúa como un tutor amable y divertido para un niño de primaria llamado {user_name} de {user_data['age']} años.
Analiza la siguiente entrada: "{user_input}"

1.  **Verifica si es una operación matemática válida** (suma, resta, multiplicación, división usando x, %, +, -). Si no es una operación, responde amablemente que solo puedes ayudar con matemáticas.
2.  **Si es una operación:**
    * **Di si la operación está correcta.**
    * **Si está mal, explícalo paso a paso de forma sencilla.** Usa emojis y ejemplos fáciles.
    * **Identifica el tipo de operación** (suma, resta, multiplicación, división) si está mal. Esto es crucial.
    * **Hazlo divertido y claro.**
3.  **Importante:** Cuando expliques un error, menciona específicamente el tipo de operación. Por ejemplo: "¡Uy, {user_name}! Parece que esa **multiplicación** tiene un pequeño error. ¡Vamos a verla juntos!" o "Bien hecho con esa **suma**".
4.  **No preguntes más nada, solo responde la evaluación o explicación.**
"""
        reply = ""
        try:
            response = model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=512
                )
            )

            if response and response.text:
                reply = response.text.strip()
            else:
                reply = f"Lo siento, {user_name}, no pude generar una respuesta. Por favor, inténtalo de nuevo."

        except Exception as e:
            reply = f"¡Ups, {user_name}! Parece que tengo un problema para pensar en este momento. Intenta de nuevo más tarde."
            print(f"Error en handle_message al generar contenido con Gemini: {e}") # Para depuración

        # --- Actualiza el conteo y el tipo de error ---
        is_incorrect = any(word in reply.lower() for word in ["incorrecto", "no es correcto", "mal", "error"])

        if is_incorrect:
            user_data["errores"] += 1
            # Intentar extraer el tipo de operación del error usando expresiones regulares
            if re.search(r'\b(multiplicación|multiplicacion)\b', reply.lower()):
                user_data["last_error_type"] = "multiplicacion"
            elif re.search(r'\b(división|division)\b', reply.lower()):
                user_data["last_error_type"] = "division"
            elif re.search(r'\b(suma)\b', reply.lower()):
                user_data["last_error_type"] = "suma"
            elif re.search(r'\b(resta)\b', reply.lower()):
                user_data["last_error_type"] = "resta"
            else:
                user_data["last_error_type"] = "general" # Para errores no específicos
        else:
            user_data["aciertos"] += 1
            user_data["last_error_type"] = None # Resetear si el ejercicio fue correcto

        save_memory() # Guarda los cambios

        # Add the recurring message here
        keyboard = [
            [InlineKeyboardButton("🆘 Necesito ayuda", callback_data="help")],
            [InlineKeyboardButton("👋 Terminar", callback_data="end_chat")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            f"{reply}\n\n¡Puedes seguir escribiendo más operaciones matemáticas! Estoy aquí para ayudarte.",
            reply_markup=reply_markup
        )

# Manejar botones
async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja las interacciones con los botones inline."""
    query = update.callback_query
    await query.answer() # Siempre responde a la callback query

    user_id = str(query.from_user.id)
    user_data = get_user_data(user_id) # Obtiene los datos del usuario

    user_name = user_data["name"] if user_data["name"] else "niño(a)" # Usar el nombre si está disponible

    if query.data == "help":
        stats = user_data # Los datos ya están cargados por get_user_data
        await query.edit_message_text(
            f"📊 Tus avances, {user_name}:\n✅ Aciertos: {stats['aciertos']}\n❌ Errores: {stats['errores']}\n¡Sigue practicando!"
        )

    elif query.data == "end_chat":
        stats = user_data
        final_message = (
            f"¡Adiós, {user_name}! 👋 Ha sido un placer ayudarte con tus matemáticas.\n"
            f"Tus resultados finales son:\n"
            f"✅ Aciertos: {stats['aciertos']}\n"
            f"❌ Errores: {stats['errores']}\n\n"
            "¡Espero verte de nuevo pronto para seguir aprendiendo! 😊"
        )
        # Opcional: borrar datos del usuario para "resetear" la conversación
        # del memory.json. Si no quieres borrar, simplemente omite estas líneas.
        if user_id in memory:
            del memory[user_id]
            save_memory()

        await query.edit_message_text(final_message)


# --- Función Principal ---

def main():
    """Configura y ejecuta el bot de Telegram."""
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Añadir handlers para los comandos y mensajes
    app.add_handler(CommandHandler("start", start))
    # El MessageHandler ahora maneja tanto la configuración inicial como las operaciones
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(handle_button))

    print("Bot corriendo...")
    app.run_polling()

if __name__ == "__main__":
    main()
