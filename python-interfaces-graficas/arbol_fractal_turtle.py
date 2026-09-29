import turtle

def draw_branch(branch_length, t):
    if branch_length > 5:  # Longitud mínima para seguir dibujando
        t.forward(branch_length)  # Dibuja la rama
        t.right(20)  # Gira a la derecha
        draw_branch(branch_length - 15, t)  # Dibuja la rama derecha
        t.left(40)  # Gira a la izquierda
        draw_branch(branch_length - 15, t)  # Dibuja la rama izquierda
        t.right(20)  # Regresa a la posición original
        t.backward(branch_length)  # Regresa a la base de la rama

# Configura la ventana de dibujo
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Color de fondo

# Crea la tortuga
t = turtle.Turtle()
t.color("brown")  # Color de la rama
t.pensize(2)  # Grosor de la línea
t.left(90)  # Orientación inicial
t.up()
t.backward(100)  # Mueve la tortuga hacia abajo
t.down()

# Dibuja el árbol
draw_branch(100, t)

# Finaliza
turtle.done()
