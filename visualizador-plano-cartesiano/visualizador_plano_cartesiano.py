import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Función para actualizar la gráfica y el texto descriptivo
def actualizar_grafica():
    try:
        # Obtener valores de entrada de las cajas de texto para X y Y
        valores_x = [int(caja_x[i].get()) for i in range(4)]  # Extrae valores de las cajas de entrada X
        valores_y = [int(caja_y[i].get()) for i in range(4)]  # Extrae valores de las cajas de entrada Y
        
        # Limpiar la gráfica anterior
        eje.clear()
        
        # Graficar la línea en color negro y puntos de inicio (azul) y fin (rojo)
        eje.plot(valores_x, valores_y, marker='o', color='black', linestyle='-', label="Línea de datos")
        eje.plot(valores_x[0], valores_y[0], marker='o', color='blue', markersize=8, label="Inicio (punto azul)")
        eje.plot(valores_x[-1], valores_y[-1], marker='o', color='red', markersize=8, label="Final (punto rojo)")
        
        # Ajustar automáticamente los límites en función de los valores de x e y con un margen de 10 unidades
        eje.set_xlim(min(valores_x) - 10, max(valores_x) + 10)
        eje.set_ylim(min(valores_y) - 10, max(valores_y) + 10)
        
        # Etiquetas de los ejes, cuadrícula y leyenda
        eje.set_xlabel("Eje X")
        eje.set_ylabel("Eje Y")
        eje.grid(True)  # Activa la cuadrícula
        eje.legend(loc="upper left", bbox_to_anchor=(1, 1), fontsize=8)  # Coloca la leyenda a la derecha
        
        # Dibujar los ejes de referencia (línea horizontal y vertical en 0)
        eje.axhline(0, color='black', linewidth=0.5)
        eje.axvline(0, color='black', linewidth=0.5)
        
        # Ajustar el margen derecho para que haya espacio suficiente para la leyenda
        figura.subplots_adjust(right=0.55)

        # Actualizar el lienzo para reflejar la nueva gráfica
        lienzo.draw()

        # Generar texto descriptivo dinámico
        inicio = (valores_x[0], valores_y[0])  # Coordenadas de inicio
        maximo = (valores_x[valores_y.index(max(valores_y))], max(valores_y))  # Coordenadas del valor máximo en Y
        minimo = (valores_x[valores_y.index(min(valores_y))], min(valores_y))  # Coordenadas del valor mínimo en Y
        
        # Determinar si la gráfica es ascendente, descendente o estable
        if valores_y[0] < valores_y[-1]:  # Compara el valor inicial con el final para ver si sube
            tendencia = "ascendente"
        elif valores_y[0] > valores_y[-1]:  # Compara el valor inicial con el final para ver si baja
            tendencia = "descendente"
        else:
            tendencia = "estable"  # Si los valores son iguales, es estable

        # Crear el texto descriptivo con la tendencia, inicio, máximo y mínimo
        texto_descriptivo = (
            f"La gráfica inicia en {inicio}, es principalmente {tendencia}, "
            f"alcanza su valor máximo en {maximo} y mínimo en {minimo}."
        )

        # Actualizar el cuadro de texto con el texto descriptivo y resaltado en color
        cuadro_texto.config(state=tk.NORMAL)  # Permitir escribir en el cuadro de texto
        cuadro_texto.delete("1.0", tk.END)  # Limpiar el texto anterior
        cuadro_texto.insert(tk.END, texto_descriptivo)  # Insertar el nuevo texto

        # Resaltar en color las palabras clave
        cuadro_texto.tag_configure("resaltado", background="yellow")  # Configurar resaltado en amarillo
        for palabra in [tendencia, str(inicio), str(maximo), str(minimo)]:  # Iterar por cada palabra clave
            indice_inicio = "1.0"  # Inicio de la búsqueda en el texto
            while True:
                indice_inicio = cuadro_texto.search(palabra, indice_inicio, tk.END)  # Buscar palabra en el texto
                if not indice_inicio:  # Si no encuentra más instancias, sale del bucle
                    break
                indice_fin = f"{indice_inicio}+{len(palabra)}c"  # Calcula el índice final de la palabra encontrada
                cuadro_texto.tag_add("resaltado", indice_inicio, indice_fin)  # Agrega la etiqueta de resaltado
                indice_inicio = indice_fin  # Continúa la búsqueda desde el final de la palabra encontrada
        
        cuadro_texto.config(state=tk.DISABLED)  # Bloquear edición del cuadro de texto

    except ValueError:
        print("Por favor, ingresa solo números enteros en los campos.")  # Manejo de errores para entradas no numéricas

# Crear la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Gráfica en Plano Cartesiano")

# Configurar tamaño inicial y centrado de la ventana
ancho_ventana = 900
alto_ventana = 700
pos_x = (ventana.winfo_screenwidth() - ancho_ventana) // 2
pos_y = (ventana.winfo_screenheight() - alto_ventana) // 2
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

# Crear la estructura de entrada en formato de cuadrícula para X y Y
caja_x = []  # Lista para almacenar entradas de X
caja_y = []  # Lista para almacenar entradas de Y

# Etiquetas para las entradas de X y Y
tk.Label(ventana, text="Puntos de Eje X:", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=4)
tk.Label(ventana, text="Puntos de Eje Y:", font=("Arial", 10, "bold")).grid(row=2, column=0, columnspan=4)

# Crear los cuadros de entrada para X y Y en filas separadas y centradas
for i in range(4):
    entrada = tk.Entry(ventana, width=5, justify='center')
    entrada.grid(row=1, column=i, padx=5, pady=5)
    caja_x.append(entrada)  # Agregar cada entrada de X a la lista

for i in range(4):
    entrada = tk.Entry(ventana, width=5, justify='center')
    entrada.grid(row=3, column=i, padx=5, pady=5)
    caja_y.append(entrada)  # Agregar cada entrada de Y a la lista

# Crear botón para actualizar la gráfica al presionarlo
boton_actualizar = tk.Button(ventana, text="Actualizar Gráfica", command=actualizar_grafica)
boton_actualizar.grid(row=4, column=0, columnspan=4, pady=10)

# Crear la figura de matplotlib para la gráfica con un tamaño adecuado
figura, eje = plt.subplots(figsize=(5, 4))  # Definir la figura y el eje para la gráfica

# Dibujar los ejes en la gráfica
eje.axhline(0, color='black', linewidth=0.5)
eje.axvline(0, color='black', linewidth=0.5)

# Etiquetas de los ejes y cuadrícula
eje.set_xlabel("Eje X")
eje.set_ylabel("Eje Y")
eje.grid(True)

# Integrar la figura de matplotlib en la ventana de tkinter
lienzo = FigureCanvasTkAgg(figura, master=ventana)
lienzo.get_tk_widget().grid(row=5, column=0, columnspan=4, pady=10)

# Crear cuadro de texto descriptivo para mostrar información de la gráfica con texto resaltado
cuadro_texto = tk.Text(ventana, height=4, width=80, font=("Arial", 10), wrap="word")
cuadro_texto.grid(row=6, column=0, columnspan=4, padx=10, pady=10)
cuadro_texto.tag_configure("resaltado", background="yellow")  # Configurar resaltado de fondo amarillo
cuadro_texto.config(state=tk.DISABLED)  # Bloquear edición inicial

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()



