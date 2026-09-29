import tkinter as tk  # Importa la biblioteca tkinter para crear interfaces gráficas.
from tkinter import messagebox  # Importa messagebox para mostrar cuadros de diálogo de mensajes.
import matplotlib.pyplot as plt  # Importa matplotlib para generar gráficos.

# Función para generar el gráfico de torta
def generar_grafico():
    categorias_filtradas = []  # Lista para almacenar las categorías ingresadas.
    valores_filtrados = []  # Lista para almacenar los valores correspondientes a las categorías.

    try:
        # Iterar sobre las entradas para categorías y valores
        for i in range(5):
            categoria = entry_cat[i].get()  # Obtiene el valor de la categoría en la posición i.
            valor = entry_val[i].get()  # Obtiene el valor correspondiente en la posición i.

            # Si la categoría y el valor no están vacíos, los agregamos a las listas filtradas
            if categoria != "" and valor != "":  # Verifica que tanto categoría como valor no estén vacíos.
                categorias_filtradas.append(categoria)  # Agrega la categoría a la lista.
                valores_filtrados.append(int(valor))  # Convierte el valor a entero y lo agrega a la lista.
        
        # Verificar que haya al menos una categoría y valor ingresado
        if len(categorias_filtradas) == 0:  # Si no se ingresaron categorías ni valores, muestra un mensaje de error.
            messagebox.showerror("Error", "Por favor, ingrese al menos una categoría y valor.")
            return  # Sale de la función si no se ingresaron valores.

        # Validar que los valores sean positivos
        if any(v < 0 for v in valores_filtrados):  # Verifica si hay valores negativos en la lista.
            messagebox.showerror("Error", "Por favor, ingrese valores positivos.")  # Muestra un error si hay valores negativos.
            return  # Sale de la función si hay valores negativos.

    except ValueError:  # Captura errores si no se puede convertir un valor a entero.
        messagebox.showerror("Error", "Por favor, ingrese solo números enteros en los valores.")  # Muestra un mensaje de error.
        return  # Sale de la función en caso de error.

    # Crear gráfico de torta
    plt.pie(valores_filtrados, labels=categorias_filtradas, autopct='%1.1f%%', startangle=90)  # Genera un gráfico de torta.
    plt.title("Gráfico de torta: Categorías")  # Agrega un título al gráfico.
    
    # Mostrar gráfico
    plt.show()  # Muestra el gráfico de torta en una ventana emergente.

# Configuración de la ventana principal
root = tk.Tk()  # Crea una ventana principal con tkinter.
root.title("Ingreso de categorías y valores para gráfico de torta")  # Establece el título de la ventana.

# Crear etiquetas y entradas para las categorías y valores
label_cat = tk.Label(root, text="Categoría")  # Crea una etiqueta para la columna de categorías.
label_cat.grid(row=0, column=0)  # Coloca la etiqueta en la primera fila, primera columna.
label_val = tk.Label(root, text="Valor")  # Crea una etiqueta para la columna de valores.
label_val.grid(row=0, column=1)  # Coloca la etiqueta en la primera fila, segunda columna.

entry_cat = []  # Lista para almacenar las entradas de las categorías.
entry_val = []  # Lista para almacenar las entradas de los valores.

for i in range(5):
    # Entrada para la categoría (texto)
    entry_cat.append(tk.Entry(root))  # Crea una entrada de texto para la categoría y la agrega a la lista.
    entry_cat[i].grid(row=i+1, column=0)  # Coloca la entrada en la fila i+1, columna 0.
    
    # Entrada para el valor (números)
    entry_val.append(tk.Entry(root))  # Crea una entrada de texto para el valor y la agrega a la lista.
    entry_val[i].grid(row=i+1, column=1)  # Coloca la entrada en la fila i+1, columna 1.

# Botón para generar el gráfico
boton = tk.Button(root, text="Diseñar gráfico", command=generar_grafico)  # Crea un botón que ejecuta la función generar_grafico.
boton.grid(row=6, columnspan=2, pady=10)  # Coloca el botón en la fila 6, ocupando dos columnas y añade espacio vertical.

# Ejecutar la ventana
root.mainloop()  # Inicia el bucle principal de la ventana para que se mantenga abierta.
