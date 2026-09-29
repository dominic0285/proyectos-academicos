import tkinter as tk  # Importar Tkinter para crear la interfaz gráfica
import random  # Importar la librería random para generar colores aleatorios

# Función que se ejecuta cuando se hace clic en el triángulo
def cambiar_color(event):
    # Generar un color aleatorio en formato hexadecimal (como #RRGGBB)
    nuevo_color = f'#{random.randint(0, 0xFFFFFF):06x}'
    
    # Cambiar el color de relleno del triángulo con el nuevo color generado
    canvas.itemconfig(triangulo, fill=nuevo_color)

# Crear la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Triángulo de Color Cambiante")  # Título de la ventana

# Establecer el tamaño de la ventana (800x600 píxeles)
ventana.geometry("800x600")  # Cambia el tamaño si lo necesitas
ventana.resizable(True, True)  # Permitir redimensionar la ventana horizontal y verticalmente

# Crear un lienzo (canvas) que ocupe toda la ventana
canvas = tk.Canvas(ventana, bg="white")  # Fondo blanco del canvas
canvas.pack(fill=tk.BOTH, expand=True)  # El canvas se expande para llenar la ventana

# Definir las coordenadas del triángulo para que esté centrado en la ventana
canvas_width = 800  # Ancho del canvas
canvas_height = 600  # Altura del canvas
# Definir las tres esquinas del triángulo
triangulo_coords = (canvas_width // 2, canvas_height // 4,  # Vértice superior
                    canvas_width // 4, canvas_height * 3 // 4,  # Esquina inferior izquierda
                    canvas_width * 3 // 4, canvas_height * 3 // 4)  # Esquina inferior derecha

# Dibujar el triángulo en el canvas con un borde negro y relleno azul
triangulo = canvas.create_polygon(triangulo_coords, outline="black", fill="blue", width=2)

# Asociar la función de cambiar color con el evento de clic en el canvas
canvas.bind("<Button-1>", cambiar_color)

# Iniciar el bucle de eventos de la ventana (mantener la ventana abierta hasta que se cierre)
ventana.mainloop()
