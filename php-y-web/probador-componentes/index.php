<?php
// Incluye el archivo PHP con las funciones
include 'funciones.php';
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Probador de Componentes</title>
    <style>
     /* Aplicar fuentes globales */
body {
    font-family: "Plus Jakarta Sans", "Noto Sans", sans-serif;
    background-color: #f9f9f9;
    color: #333;
}

/* Cabecera con fecha y hora en fondo negro */
.date-time-header {
    background-color: #000000;
    color: #ffffff;
    font-weight: bold;
    padding: 10px 20px;
    font-size: 16px;
    border-bottom: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Contenedor para organizar cámara y micrófono en columnas */
.component-tester {
    display: flex;
    justify-content: space-around;
    margin: 20px 0;
    gap: 20px;
}

.component-box {
    flex: 1;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    background-color: #ffffff;
    border: 1px solid #ccc;
    text-align: center;
}

video, audio {
    width: 100%;
    max-width: 100%;
    border-radius: 8px;
    margin-top: 10px;
}

/* Botones estilo Google: negros con texto blanco */
.button {
    background-color: #000000;
    color: white;
    padding: 15px 20px;
    border: none;
    cursor: pointer;
    font-size: 16px;
    border-radius: 8px;
    transition: background-color 0.3s ease, transform 0.2s ease;
}

.button:hover {
    background-color: #333333;
    transform: scale(1.05);
}

/* Modal estilizado */
.modal {
    display: none;
    position: fixed;
    z-index: 999;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6);
    transition: opacity 0.3s ease-in-out;
}

.modal-content {
    background-color: #fff;
    margin: 10% auto;
    padding: 20px;
    border-radius: 12px;
    max-width: 900px;
    width: 90%;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Estilo para cerrar el modal */
.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
    transition: color 0.2s ease;
}

.close:hover,
.close:focus {
    color: #000;
    cursor: pointer;
}

/* Estilo de la sección de la prueba de pantalla táctil */
.touch-area {
    width: 100%;
    height: 200px;
    background-color: #f0f0f0;
    border: 2px dashed #ccc;
    border-radius: 8px;
    position: relative;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
}

.touch-output {
    font-size: 20px;
    color: #333;
}

/* Footer con copyright */
.footer-copyright {
    background-color: #000000;
    color: white;
    padding: 15px;
    text-align: center;
    font-size: 14px;
    border-top: 1px solid #ccc;
    border-radius: 0 0 8px 8px;
}

    </style>
</head>
<body>

    <div class="date-time-header">
        Probador de Componentes - Fecha y hora: <?php echo getCurrentDateTime(); ?>
    </div>

    <div class="component-tester">
        <!-- Sección de la cámara -->
        <div>
            <h2>Probador de Cámara</h2>
            <video id="video" autoplay></video>
            <br>
            <button class="button" onclick="startCamera()">Iniciar Cámara</button>
            <button class="button" onclick="stopCamera()">Apagar Cámara</button>
        </div>

        <!-- Sección del micrófono -->
        <div>
            <h2>Probador de Micrófono</h2>
            <audio id="audio" controls></audio>
            <br>
            <button class="button" onclick="startMicrophone()">Iniciar Micrófono</button>
            <canvas id="micVisualizer" width="600" height="100"></canvas> <!-- Canvas para la gráfica -->
        </div>
    </div>


    <!-- Sección del teclado -->
    <div>
        <h2>Probador de Teclado</h2>
        <p>Escribe algo en el campo de abajo y verás lo que escribes:</p>
        <input type="text" id="keyboardInput" oninput="showKey(this.value)" placeholder="Escribe aquí..." style="padding:10px; width:100%; max-width: 600px; border-radius: 8px; border: 1px solid #ccc;">
        <p id="output"></p>
    </div>

    <!-- Sección para probar la pantalla táctil -->
    <div class="touch-test">
        <h2>Prueba de Pantalla Táctil</h2>
        <div class="touch-area" id="touchArea" onclick="showTouchPosition(event)">
            <div class="touch-output" id="touchOutput">Toca aquí</div>
        </div>
    </div>

    <!-- Footer con Copyright -->
    <div class="footer-copyright">
        &copy; <?php echo date("Y"); ?> Probador de Componentes. Todos los derechos reservados.
    </div>

    <!-- Incluir el script mediante PHP -->
    <?php includeScript(); ?>

</body>
</html>
