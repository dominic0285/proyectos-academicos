import tkinter as tk
from tkinter import ttk

def reorganizar_alfabeto(clave, alfabeto_base):
    """Reorganiza el alfabeto base según el orden de las letras en la clave."""
    orden_clave = sorted(list(clave))
    alfabeto_reorganizado = {}
    letras_usadas = set()
    
    # Primero, añade las letras de la clave al alfabeto reorganizado
    for letra in orden_clave:
        if letra.upper() in alfabeto_base and letra.upper() not in letras_usadas:
            alfabeto_reorganizado[letra.upper()] = alfabeto_base[letra.upper()]
            letras_usadas.add(letra.upper())
    
    # Luego, añade las letras restantes del alfabeto base
    for letra, valor in alfabeto_base.items():
        if letra not in letras_usadas:
            alfabeto_reorganizado[letra] = valor
            
    return alfabeto_reorganizado

def cifrar(mensaje, clave, alfabeto_base):
    """Cifra el mensaje utilizando el alfabeto reorganizado."""
    alfabeto_reorganizado = reorganizar_alfabeto(clave, alfabeto_base)
    mensaje_cifrado = ''
    for letra in mensaje.upper():
        if letra in alfabeto_reorganizado:
            mensaje_cifrado += alfabeto_reorganizado[letra]
        else:
            mensaje_cifrado += letra  # Si no está en el alfabeto, deja el caracter original
    return mensaje_cifrado

def descifrar(mensaje_cifrado, clave, alfabeto_base):
    """Descifra el mensaje cifrado utilizando el alfabeto reorganizado."""
    alfabeto_reorganizado = reorganizar_alfabeto(clave, alfabeto_base)
    
    # Invertir el alfabeto reorganizado para la búsqueda inversa
    alfabeto_inverso = {valor: letra for letra, valor in alfabeto_reorganizado.items()}
    
    mensaje_descifrado = ''
    
    #Probar con el ejemplo del mensaje HOLA
    i = 0
    while i < len(mensaje_cifrado):
        par = mensaje_cifrado[i:i+2]  #Extrae dos caracteres para buscar la letra original
        if par in alfabeto_inverso:
            mensaje_descifrado += alfabeto_inverso[par]
            i += 2  # Avanza dos posiciones porque hemos procesado un par
        else:
            mensaje_descifrado += mensaje_cifrado[i] #Si no encuentra el par, agrega el caracter original
            i += 1
    return mensaje_descifrado

def ejecutar_operacion():
    """Cifra o descifra el mensaje según la selección del usuario."""
    mensaje = mensaje_entry.get()
    clave = clave_entry.get()
    operacion = operacion_var.get()

    if operacion == "Cifrar":
        resultado = cifrar(mensaje, clave, alfabeto_base)
    else:
        resultado = descifrar(mensaje, clave, alfabeto_base)

    resultado_label.config(text="Resultado: " + resultado)

# Definir el alfabeto base
alfabeto_base = {
    'A': '1!', 'B': '2@', 'C': '3#', 'D': '4$', 'E': '5%',
    'F': '6^', 'G': '7&', 'H': '8*', 'I': '9(', 'J': '0)',
    'K': '+1', 'L': '-2', 'M': '*3', 'N': '/4', 'O': '?5',
    'P': '>6', 'Q': '<7', 'R': '=8', 'S': ':9', 'T': '{0}',
    'U': '', 'V': ']2', 'W': '"3', 'X': '~4', 'Y': "'5",
    'Z': '`6'
}

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cifrado y Descifrado")

# Crear y colocar los widgets
mensaje_label = ttk.Label(ventana, text="Mensaje:")
mensaje_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
mensaje_entry = ttk.Entry(ventana, width=30)
mensaje_entry.grid(row=0, column=1, padx=5, pady=5)

clave_label = ttk.Label(ventana, text="Clave:")
clave_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
clave_entry = ttk.Entry(ventana, width=30)
clave_entry.grid(row=1, column=1, padx=5, pady=5)

operacion_var = tk.StringVar(value="Cifrar")
cifrar_radio = ttk.Radiobutton(ventana, text="Cifrar", variable=operacion_var, value="Cifrar")
cifrar_radio.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
descifrar_radio = ttk.Radiobutton(ventana, text="Descifrar", variable=operacion_var, value="Descifrar")
descifrar_radio.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

ejecutar_button = ttk.Button(ventana, text="Ejecutar", command=ejecutar_operacion)
ejecutar_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
resultado_label = ttk.Label(ventana, text="Resultado:")
resultado_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()