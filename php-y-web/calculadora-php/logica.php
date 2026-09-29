<?php
// Importamos el archivo que contiene la función sumar
include 'funciones.php';

// Inicializamos la variable $resultado en null, para manejar la respuesta luego
$resultado = null;

// Verificamos si el formulario fue enviado usando el método POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Comprobamos si ambas claves (numero1 y numero2) existen en $_POST
    if (isset($_POST['numero1']) && isset($_POST['numero2'])) {
        // Capturamos los valores enviados desde el formulario
        $numero1 = $_POST['numero1'];
        $numero2 = $_POST['numero2'];

        // Llamamos a la función sumar que está en funciones.php y guardamos el resultado
        $resultado = sumar($numero1, $numero2);
    }
}
?>
