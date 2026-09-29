import tkinter as tk  # Importar tkinter para la interfaz gráfica
from tkinter import messagebox  # Importar messagebox para mostrar mensajes emergentes
import matplotlib.pyplot as plt  # Importar matplotlib para realizar calculos 

# Función para generar un gráfico de barras con categorías (X) y cantidades vendidas (Y)
def generar_grafico():
    try:
        # Obtener los valores de las entradas en la interfaz
        x_vals = [entry_x[i].get() for i in range(5)]  # Obtener los textos de categorías (X)
        y_vals = [int(entry_y[i].get()) for i in range(5)]  # Obtener los valores numéricos de Y
        precios = [float(entry_precio[i].get()) for i in range(5)]  # Obtener los precios por unidad
    except ValueError:
        # Si hay un error en los datos (no son números), mostrar un mensaje de error
        messagebox.showerror("Error", "Por favor, ingrese solo números válidos.")
        return

    # Crear el gráfico de barras con los valores de X e Y
    plt.bar(x_vals, y_vals, color='blue', alpha=0.7)

    # Añadir etiquetas y título al gráfico
    plt.xlabel('Categorías')  # Etiqueta para el eje X
    plt.ylabel('Cantidad Vendida')  # Etiqueta para el eje Y
    plt.title('Gráfico de barras de ventas')  # Título del gráfico

    # Mostrar el gráfico en una ventana emergente
    plt.show()

# Función para calcular y mostrar el total de ventas
def mostrar_total_ventas():
    try:
        # Obtener los valores de las entradas Y y Precio
        y_vals = [int(entry_y[i].get()) for i in range(5)]  # Cantidades vendidas (Y)
        precios = [float(entry_precio[i].get()) for i in range(5)]  # Precios por unidad
    except ValueError:
        # Si hay error en los datos (no son números), mostrar un mensaje de error
        messagebox.showerror("Error", "Por favor, ingrese solo números válidos.")
        return

    # Calcular el total generado por las ventas multiplicando cantidad por precio
    total_ventas = sum(y * p for y, p in zip(y_vals, precios))
    
    # Mostrar el total de ventas en un mensaje emergente
    messagebox.showinfo("Total de Ventas", f"Total generado: ${total_ventas:.2f}")

# Configuración de la ventana principal
root = tk.Tk()  # Crear la ventana principal
root.title("Ingreso de categorías y diseño de gráfico")  # Establecer el título de la ventana

# Crear etiquetas para las columnas de entrada
label_x = tk.Label(root, text="Categorías (X)")  # Etiqueta para las categorías (X)
label_x.grid(row=0, column=0)  # Posicionar la etiqueta en la primera fila, primera columna
label_y = tk.Label(root, text="Cantidad Vendida (Y)")  # Etiqueta para la cantidad vendida (Y)
label_y.grid(row=0, column=1)  # Posicionar en la primera fila, segunda columna
label_precio = tk.Label(root, text="Precio por Unidad ($)")  # Etiqueta para el precio por unidad
label_precio.grid(row=0, column=2)  # Posicionar en la primera fila, tercera columna

# Crear listas para almacenar las entradas de texto (categorías, cantidades y precios)
entry_x = []  # Lista para las entradas de categorías
entry_y = []  # Lista para las entradas de cantidades
entry_precio = []  # Lista para las entradas de precios

# Bucle para crear cinco filas de entradas
for i in range(5):
    # Crear entrada para las categorías (X) y posicionarla
    entry_x.append(tk.Entry(root))
    entry_x[i].grid(row=i+1, column=0)  # Posicionar las entradas de categorías en la columna 0
    
    # Crear entrada para las cantidades (Y) y posicionarla
    entry_y.append(tk.Entry(root))
    entry_y[i].grid(row=i+1, column=1)  # Posicionar las entradas de cantidades en la columna 1
    
    # Crear entrada para los precios y posicionarla
    entry_precio.append(tk.Entry(root))
    entry_precio[i].grid(row=i+1, column=2)  # Posicionar las entradas de precios en la columna 2

# Crear botón para generar el gráfico
boton_grafico = tk.Button(root, text="Diseñar gráfico", command=generar_grafico)
boton_grafico.grid(row=6, columnspan=3, pady=5)  # Posicionar el botón en una nueva fila

# Crear botón para calcular y mostrar el total de ventas
boton_total = tk.Button(root, text="Mostrar total de ventas", command=mostrar_total_ventas)
boton_total.grid(row=7, columnspan=3, pady=5)  # Posicionar el botón debajo del anterior

# Iniciar la ventana principal
root.mainloop()  # Mantener la ventana abierta hasta que el usuario la cierre
