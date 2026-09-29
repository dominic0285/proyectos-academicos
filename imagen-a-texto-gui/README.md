# Image to Text Converter GUI

Este proyecto es una aplicación de escritorio desarrollada en Python usando `tkinter` y `Pillow` que permite:

- Convertir una imagen en un archivo de texto con sus datos (modo, tamaño, y píxeles).
- Reconstruir la imagen original a partir de ese archivo de texto.

### 🧠 ¿Cómo funciona?

El programa ofrece una interfaz gráfica sencilla con dos botones:

- **Cifrar Imagen**: Seleccionas una imagen y la convierte en un archivo `.txt` que contiene:
  - Dimensiones de la imagen
  - Modo de color (RGB, RGBA, L)
  - Todos los píxeles codificados

- **Descifrar Texto**: A partir del archivo `.txt` generado, se reconstruye la imagen original.

### 💡 Tecnologías utilizadas

- Python 3.x
- Tkinter (interfaz gráfica)
- Pillow (`PIL`) para manipular imágenes

### 📦 Instalación

1. Asegúrate de tener Python instalado.
2. Instala Pillow si no lo tienes:

```bash
pip install pillow

autor 
Dominic De Freitas