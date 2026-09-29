# Tutor de Matemáticas para Telegram 🤖➕➗

Este es un bot de Telegram desarrollado en Python que actúa como un tutor virtual de matemáticas para niños de primaria. Utiliza la API de **Gemini** (IA de Google) para entender operaciones matemáticas y dar retroalimentación divertida, educativa y adaptada a la edad del estudiante.

---

## 🧰 Tecnologías utilizadas

- **Python 3**
- **Telegram Bot API** – Manejo de interacciones con usuarios.
- **Google Gemini API** – Para generar explicaciones inteligentes.
- **dotenv** – Manejo de variables de entorno.
- **json** – Almacenamiento de datos de usuario.
- **regex (re)** – Identificación de tipos de operación.

---

## 🎯 Funcionalidades

- Registro de nombre y edad del niño.
- Comprensión de operaciones como suma (`+`), resta (`-`), multiplicación (`x`), y división (`%`).
- Retroalimentación divertida y personalizada usando Gemini.
- Cuenta aciertos y errores del usuario.
- Usa botones interactivos de Telegram para pedir ayuda o terminar la sesión.
- Guarda el estado de cada usuario en un archivo local `memory.json`.

---

## ⚙️ Cómo usar

### 1. Clona el repositorio
```bash
git clone https://github.com/dominic0285/tutor-matematicas-telegram-bot.git
cd tutor-matematicas-telegram-bot
