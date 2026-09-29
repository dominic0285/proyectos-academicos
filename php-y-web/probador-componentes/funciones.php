<?php
// funciones.php

// Establecer la zona horaria 
date_default_timezone_set("America/Caracas");

// Función para incluir el archivo JavaScript dinámicamente
function includeScript() {
    echo '<script src="script.js"></script>';
}

// Función para obtener la fecha y hora actual
function getCurrentDateTime() {
     return date("Y-m-d h:i:s A"); // Formato de 12 horas con AM/PM
}
?>
