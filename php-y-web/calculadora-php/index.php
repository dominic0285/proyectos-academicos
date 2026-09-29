<?php
// Incluimos el archivo logica.php, que maneja la lógica de la suma
include 'logica.php';
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8"> <!-- Definimos el conjunto de caracteres como UTF-8 -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Para diseño adaptable a diferentes dispositivos -->
    <title>Calculadora de Suma</title> <!-- Título de la página -->
    <style>
        /* Estilos globales para el cuerpo */
        body {
            font-family: 'Arial', sans-serif; /* Fuente para todo el cuerpo */
            background-color: #eef2f7; /* Color de fondo suave */
            display: flex; /* Usamos Flexbox para centrar el contenido */
            justify-content: center; /* Centramos horizontalmente */
            align-items: center; /* Centramos verticalmente */
            height: 100vh; /* Hacemos que el cuerpo ocupe el 100% del alto de la ventana */
            margin: 0; /* Eliminamos el margen predeterminado */
        }

        /* Estilos para el contenedor principal de la calculadora */
        .container {
            background-color: white; /* Fondo blanco para el contenedor */
            padding: 30px; /* Espaciado interno */
            border-radius: 15px; /* Bordes redondeados */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra suave */
            max-width: 400px; /* Tamaño máximo del contenedor */
            width: 100%; /* El ancho se ajusta al 100% de su contenedor padre */
        }

        /* Estilos para el encabezado */
        .header {
            text-align: center; /* Centramos el texto */
            margin-bottom: 20px; /* Añadimos margen inferior */
            color: #4A90E2; /* Color del texto */
        }

        /* Estilo del título principal */
        h2 {
            margin: 0; /* Eliminamos margen */
            font-size: 1.8em; /* Tamaño de fuente grande */
        }

        /* Estilos para el formulario */
        form {
            display: flex; /* Usamos Flexbox para los elementos del formulario */
            flex-direction: column; /* Los elementos del formulario se apilan verticalmente */
        }

        /* Estilos para los campos de entrada de número y resultado */
        input[type="number"], input[type="text"] {
            padding: 10px; /* Espaciado interno */
            margin: 10px 0; /* Margen superior e inferior */
            border: 1px solid #ddd; /* Borde gris claro */
            border-radius: 10px; /* Bordes redondeados */
            font-size: 1em; /* Tamaño de fuente mediano */
            box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1); /* Sombra interior */
        }

        /* Caja de texto para mostrar el resultado (deshabilitada) */
        input[type="text"]:disabled {
            background-color: #f9f9f9; /* Color de fondo gris claro */
        }

        /* Estilos para el botón de envío */
        input[type="submit"] {
            padding: 12px; /* Espaciado interno del botón */
            margin-top: 10px; /* Margen superior */
            background-color: #4CAF50; /* Color de fondo del botón */
            color: white; /* Texto blanco */
            border: none; /* Sin bordes */
            border-radius: 10px; /* Bordes redondeados */
            font-size: 1em; /* Tamaño de fuente mediano */
            cursor: pointer; /* El cursor cambia al pasar sobre el botón */
            transition: background-color 0.3s ease; /* Transición suave del color de fondo al hacer hover */
        }

        /* Cambiamos el color de fondo del botón cuando se pasa el mouse por encima */
        input[type="submit"]:hover {
            background-color: #45a049; /* Color verde más oscuro */
        }
    </style>
</head>
<body>
    <!-- Contenedor principal de la calculadora -->
    <div class="container">
        <!-- Encabezado de la calculadora -->
        <div class="header">
            <h2>Calculadora de Suma</h2> <!-- Título de la calculadora -->
        </div>
        <!-- Formulario para ingresar los números y mostrar el resultado -->
        <form method="POST">
            <!-- Campo de entrada para el primer número -->
            <input type="number" name="numero1" placeholder="Número 1" required>
            <!-- Campo de entrada para el segundo número -->
            <input type="number" name="numero2" placeholder="Número 2" required>
            <!-- Caja de texto deshabilitada para mostrar el resultado -->
            <input type="text" placeholder="Resultado" value="<?php echo $resultado !== null ? $resultado : ''; ?>" disabled>
            <!-- Botón para calcular -->
            <input type="submit" value="Calcular">
        </form>
    </div>
</body>
</html>
