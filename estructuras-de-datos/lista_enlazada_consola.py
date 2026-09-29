import random
import os
# Clase Nodo para la lista enlazada
class Nodo:
    # Constructor que inicializa un nodo con el valor dado
    def __init__(self, dato):
        self.dato = dato  # Almacena el valor del nodo
        self.siguiente = None  # Apuntador al siguiente nodo, inicialmente es None

# Clase ListaEnlazada para gestionar la estructura de la lista enlazada
class ListaEnlazada:
    # Constructor que inicializa una lista enlazada vacía
    def __init__(self):
        self.cabeza = None  # El primer nodo (cabeza) de la lista, inicialmente None
        self.tamano = 0  # Tamaño de la lista, inicialmente 0

    # Método para agregar un valor a la lista enlazada
    def agregar(self, valor):
        if self.tamano < 5:  # Limitar el número de nodos a 5
            nuevo_nodo = Nodo(valor)  # Crear un nuevo nodo con el valor dado
            if self.cabeza is None:  # Si la lista está vacía
                self.cabeza = nuevo_nodo  # El nuevo nodo se convierte en la cabeza de la lista
            else:
                actual = self.cabeza  # Iniciar desde la cabeza
                # Recorrer la lista hasta llegar al último nodo
                while actual.siguiente:
                    actual = actual.siguiente
                # Agregar el nuevo nodo al final de la lista
                actual.siguiente = nuevo_nodo
            self.tamano += 1  # Incrementar el tamaño de la lista en 1
        else:
            # Si la lista ya tiene 5 elementos, no se permite agregar más
            print("La lista ya está llena.")

    # Método para obtener todos los valores de la lista como una lista de Python
    def obtener_lista(self):
        lista = []  # Crear una lista vacía para almacenar los valores
        actual = self.cabeza  # Empezar desde la cabeza de la lista enlazada
        # Recorrer la lista enlazada hasta el final
        while actual:
            lista.append(actual.dato)  # Agregar el valor del nodo actual a la lista
            actual = actual.siguiente  # Avanzar al siguiente nodo
        return lista  # Retornar la lista de valores

    # Método para mostrar visualmente la lista enlazada en la consola
    def mostrar_lista(self):
        actual = self.cabeza  # Iniciar desde la cabeza de la lista
        # Recorrer toda la lista enlazada
        while actual:
            # Mostrar el valor del nodo dentro de un cuadro
            print(f"╔═══╗\n║ {actual.dato} ║ ")
            actual = actual.siguiente  # Avanzar al siguiente nodo
        # Al final de la lista, mostrar "NULL" indicando el fin
        print("NULL")

# Función para llenar la Lista 3 con elementos aleatorios de las Listas 1 y 2
def llenar_lista3(lista1, lista2, lista3):
    # Obtener los valores de la Lista 1 y la Lista 2
    valores_lista1 = lista1.obtener_lista()
    valores_lista2 = lista2.obtener_lista()

    # Verificar que ambas listas tengan al menos 5 valores
    if len(valores_lista1) < 5 or len(valores_lista2) < 5:
        print("Las listas 1 y 2 deben tener al menos 5 valores.")
        return

    # Combinar los valores de ambas listas en una sola lista
    combinada = valores_lista1 + valores_lista2

    # Reiniciar la Lista 3 (vaciarla)
    lista3.__init__()

    # Seleccionar 5 valores aleatorios de la lista combinada
    for _ in range(5):
        valor_aleatorio = random.choice(combinada)  # Seleccionar un valor aleatorio
        lista3.agregar(valor_aleatorio)  # Agregar ese valor a la Lista 3
        combinada.remove(valor_aleatorio)  # Eliminar el valor seleccionado de la lista combinada

    # Mostrar la Lista 3 en consola
    print("\nLista 3 (Aleatoria):")
    lista3.mostrar_lista()
    

# Función principal que ejecuta el programa
if __name__ == "__main__":
    # Inicializar las tres listas enlazadas (vacías)
    lista1 = ListaEnlazada()
    lista2 = ListaEnlazada()
    lista3 = ListaEnlazada()

    # Llenar la Lista 1 con 5 números proporcionados por el usuario
    print("Ingresa 5 números para la Lista 1:")
    for i in range(5):
        valor = int(input(f"Número {i + 1}: "))  # Solicitar número al usuario
        lista1.agregar(valor)  # Agregar el número a la Lista 1

    # Mostrar la Lista 1
    print("\nLista 1:")
    lista1.mostrar_lista()

    # Llenar la Lista 2 con 5 números proporcionados por el usuario
    print("\nIngresa 5 números para la Lista 2:")
    for i in range(5):
        valor = int(input(f"Número {i + 1}: "))  # Solicitar número al usuario
        lista2.agregar(valor)  # Agregar el número a la Lista 2

    # Mostrar la Lista 2
    print("\nLista 2:")
    lista2.mostrar_lista()

    # Llenar y mostrar la Lista 3 con elementos aleatorios seleccionados de las Listas 1 y 2
    llenar_lista3(lista1, lista2, lista3)
os.system("pause")
