<?php
// Se incluye la biblioteca de corrección ortográfica
require_once('spellcheck_library.php');

// Se verifica si la solicitud es de tipo POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Se obtiene el texto enviado desde el formulario
    $text = $_POST['text'];
    
    // Se llama a la función checkSpelling para verificar la ortografía del texto
    $result = checkSpelling($text);
    
    // Se muestra el resultado de la corrección ortográfica
    echo $result;
}
?>
