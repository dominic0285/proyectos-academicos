import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image

def imagen_a_texto(ruta_imagen, ruta_texto):
    """
    Convierte una imagen en un archivo de texto que contiene información sobre sus dimensiones,
    modo y los píxeles.
    """
    try:
        # Abrir la imagen a partir de la ruta proporcionada
        imagen = Image.open(ruta_imagen)
        ancho, alto = imagen.size  # Obtener el ancho y alto de la imagen
        lista_pixeles = list(imagen.getdata())  # Extraer la lista de píxeles
    except Exception as error:
        messagebox.showerror("Error", f"No se pudo abrir la imagen: {error}")
        return

    try:
        # Abrir (o crear) el archivo de texto para escribir los datos de la imagen
        with open(ruta_texto, 'w') as archivo:
            # Guardar en la primera línea: ancho, alto y modo (ejemplo: RGB, L, RGBA, etc.)
            archivo.write(f"{ancho} {alto} {imagen.mode}\n")
            # Recorrer cada fila de píxeles de la imagen
            for fila in range(alto):
                # Extraer los píxeles correspondientes a la fila actual
                linea_pixeles = lista_pixeles[fila * ancho:(fila + 1) * ancho]
                # Convertir cada píxel a cadena ("R,G,B" o "R,G,B,A" o valor único para escala de grises)
                linea = " ".join(
                    [",".join(map(str, pixel)) if isinstance(pixel, tuple) else str(pixel)
                     for pixel in linea_pixeles]
                )
                archivo.write(linea + "\n")
        messagebox.showinfo("Éxito", "La imagen se ha cifrado a texto correctamente.")
    except Exception as error:
        messagebox.showerror("Error", f"No se pudo guardar el archivo de texto: {error}")

def texto_a_imagen(ruta_texto, ruta_imagen):
    """
    Reconstruye una imagen a partir de un archivo de texto que contiene su información.
    """
    try:
        # Abrir el archivo de texto que contiene los datos de la imagen
        with open(ruta_texto, 'r') as archivo:
            # Leer la primera línea para obtener ancho, alto y modo
            encabezado = archivo.readline().strip().split()
            ancho, alto, modo = int(encabezado[0]), int(encabezado[1]), encabezado[2]
            lista_pixeles = []
            # Leer cada línea del archivo para reconstruir los píxeles
            for linea in archivo:
                for valor in linea.strip().split():
                    if modo == "RGB":
                        r, g, b = map(int, valor.split(","))
                        lista_pixeles.append((r, g, b))
                    elif modo == "RGBA":
                        r, g, b, a = map(int, valor.split(","))
                        lista_pixeles.append((r, g, b, a))
                    elif modo == "L":
                        lista_pixeles.append(int(valor))
                    else:
                        # Para otros modos, se guarda el valor tal cual (aunque podría generar error si no es int o tupla)
                        lista_pixeles.append(valor)
    except Exception as error:
        messagebox.showerror("Error", f"No se pudo leer el archivo de texto: {error}")
        return

    try:
        # Crear una nueva imagen con el modo y las dimensiones especificadas
        imagen = Image.new(modo, (ancho, alto))
        imagen.putdata(lista_pixeles)
        imagen.save(ruta_imagen)
        messagebox.showinfo("Éxito", "El texto se ha descifrado a imagen correctamente.")
    except Exception as error:
        messagebox.showerror("Error", f"No se pudo guardar la imagen: {error}")

def codificar_imagen():
    """
    Permite al usuario seleccionar una imagen y guardarla como archivo de texto.
    """
    ruta_imagen = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if not ruta_imagen:
        return
    ruta_texto = filedialog.asksaveasfilename(
        title="Guardar archivo de texto como",
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt")]
    )
    if not ruta_texto:
        return
    imagen_a_texto(ruta_imagen, ruta_texto)

def decodificar_texto():
    """
    Permite al usuario seleccionar un archivo de texto y reconstruir la imagen a partir de él.
    """
    ruta_texto = filedialog.askopenfilename(
        title="Selecciona un archivo de texto",
        filetypes=[("Archivos de texto", "*.txt")]
    )
    if not ruta_texto:
        return
    ruta_imagen = filedialog.asksaveasfilename(
        title="Guardar imagen como",
        defaultextension=".png",
        filetypes=[("Imagen PNG", "*.png"), ("Imagen JPEG", "*.jpg;*.jpeg")]
    )
    if not ruta_imagen:
        return
    texto_a_imagen(ruta_texto, ruta_imagen)

# Crear la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Cifrado/Descifrado de Imagen a Texto")

# Configurar el estilo usando ttk para una apariencia moderna
estilo = ttk.Style()
estilo.configure("TFrame", background="#f0f0f0")
estilo.configure("TButton", font=("Helvetica", 12), padding=10)
estilo.configure("TLabel", background="#f0f0f0", font=("Helvetica", 14))

# Crear un marco principal con padding para organizar los elementos de la interfaz
marco_principal = ttk.Frame(ventana, padding="20 20 20 20")
marco_principal.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# Etiqueta de título de la aplicación
etiqueta_titulo = ttk.Label(
    marco_principal,
    text="Cifrado y Descifrado de Imagen a Texto",
    font=("Helvetica", 18, "bold")
)
etiqueta_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Botón para cifrar la imagen (convertir imagen a texto)
boton_codificar = ttk.Button(
    marco_principal,
    text="Cifrar Imagen (Imagen a Texto)",
    command=codificar_imagen
)
boton_codificar.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Botón para descifrar el texto (convertir texto a imagen)
boton_decodificar = ttk.Button(
    marco_principal,
    text="Descifrar Texto (Texto a Imagen)",
    command=decodificar_texto
)
boton_decodificar.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Configurar la expansión de las columnas para que se ajusten al tamaño de la ventana
marco_principal.columnconfigure(0, weight=1)
marco_principal.columnconfigure(1, weight=1)

# Establecer un tamaño mínimo para la ventana
ventana.minsize(500, 200)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
