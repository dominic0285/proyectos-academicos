let videoStream;  // Variable para almacenar el stream de video
let audioContext, analyser, microphone, javascriptNode;
const canvas = document.getElementById('micVisualizer');
const canvasContext = canvas.getContext('2d');
let audioStream;  // Variable para almacenar el stream de audio

// Función para iniciar la cámara (lado cliente)
function startCamera() {
    // Solicitar acceso a la cámara (solo video, sin audio)
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
            // Guardar el stream de video en la variable global
            videoStream = stream;
            
            // Obtener el elemento de video del DOM
            var video = document.getElementById('video');
            
            // Asignar el stream de video al elemento video para mostrarlo
            video.srcObject = stream;
        })
        .catch(function(error) {
            // Mostrar un mensaje de alerta si hay un error al acceder a la cámara
            alert("Error al acceder a la cámara: " + error.message);
        });
}

// Función para apagar la cámara
function stopCamera() {
    // Verificar si hay un stream de video activo
    if (videoStream) {
        // Detener todas las pistas (tracks) del stream para apagar la cámara
        videoStream.getTracks().forEach(track => track.stop());
        
        // Remover el stream de video del elemento video
        document.getElementById('video').srcObject = null;
    }
}

// Función para iniciar el micrófono y la gráfica
function startMicrophone() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(function(stream) {
            // Guardar el stream de audio para su uso en el elemento <audio>
            audioStream = stream;
            const audioElement = document.getElementById('audio');
            audioElement.srcObject = audioStream;

            // Inicializar el contexto de audio para la visualización
            audioContext = new (window.AudioContext || window.webkitAudioContext)();
            analyser = audioContext.createAnalyser();
            analyser.fftSize = 256;
            microphone = audioContext.createMediaStreamSource(stream);
            javascriptNode = audioContext.createScriptProcessor(2048, 1, 1);
            
            microphone.connect(analyser);
            analyser.connect(javascriptNode);
            javascriptNode.connect(audioContext.destination);

            // Procesar datos de audio y mostrar la visualización
            javascriptNode.onaudioprocess = function() {
                const dataArray = new Uint8Array(analyser.frequencyBinCount);
                analyser.getByteFrequencyData(dataArray);

                // Limpiar el canvas
                canvasContext.clearRect(0, 0, canvas.width, canvas.height);

                // Dibujar barras para representar la intensidad de sonido
                const barWidth = (canvas.width / dataArray.length) * 2.5;
                let barHeight;
                let x = 0;

                for (let i = 0; i < dataArray.length; i++) {
                    barHeight = dataArray[i];

                    canvasContext.fillStyle = 'rgb(' + (barHeight + 100) + ',50,50)';
                    canvasContext.fillRect(x, canvas.height - barHeight / 2, barWidth, barHeight / 2);

                    x += barWidth + 1;
                }
            };
        })
        .catch(function(error) {
            alert("Error al acceder al micrófono: " + error.message);
        });
}

// Función para reproducir manualmente el audio en el elemento <audio>
function playAudio() {
    const audioElement = document.getElementById('audio');
    if (audioElement.srcObject) {
        audioElement.play();  // Iniciar la reproducción
    } else {
        alert("Primero debes iniciar el micrófono.");
    }
}

// Mostrar el valor ingresado en el input de teclado
function showKey(value) {
    document.getElementById('output').innerText = "Has escrito: " + value;
}

// Mostrar la posición donde se toca en la pantalla táctil
function showTouchPosition(event) {
    const x = event.clientX;
    const y = event.clientY;
    document.getElementById('touchOutput').innerText = `Coordenadas: (${x}, ${y})`;
}
