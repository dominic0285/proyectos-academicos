<?php
// Datos de conexión a la base de datos
// Configura estos valores con variables de entorno (nunca escribas la contraseña aquí)
$servername = getenv('DB_HOST') ?: '127.0.0.1';
$username   = getenv('DB_USER') ?: 'root';
$password   = getenv('DB_PASSWORD') ?: '';
$dbname     = getenv('DB_NAME') ?: 'link_info_db';

// Conexión a la base de datos
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['url'])) {
    $url = $_POST['url'];

    // Validamos el URL
    if (filter_var($url, FILTER_VALIDATE_URL)) {
        $parsedUrl = parse_url($url, PHP_URL_HOST);
        $ip = gethostbyname($parsedUrl);
        
        // Obtenemos los registros DNS y procesamos los resultados
        $dns = dns_get_record($parsedUrl, DNS_A);
        $dnsNames = []; // Creamos un arreglo vacío para almacenar las IPs

        // Usamos un bucle en lugar de array_map para evitar el error
        foreach ($dns as $record) {
            if (isset($record['ip'])) {
                $dnsNames[] = $record['ip'];
            }
        }

        // Guardamos la IP y DNS en la base de datos
        $dnsNamesStr = implode(", ", $dnsNames);  // Guardamos el resultado en una variable
        $stmt = $conn->prepare("INSERT INTO links (url, ip, dns) VALUES (?, ?, ?)");
        $stmt->bind_param("sss", $url, $ip, $dnsNamesStr);  // Usamos la variable en lugar de llamar a implode() directamente
        $stmt->execute();
        $stmt->close();

        // Mostramos los resultados
        $result = [
            "url" => $url,
            "ip" => $ip,
            "dns" => $dnsNamesStr
        ];
    } else {
        $error = "La URL ingresada no es válida.";
    }
}

// Cerramos la conexión
$conn->close();
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Extracción de IP y DNS de una URL</title>
    <style>
        /* Importa la fuente de Material Design */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

        /* Estilos generales */
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f3f4f6;
            color: #333;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }

        h2 {
            color: #333;
        }

        /* Estilos del contenedor principal */
        .container-form {
            background-color: #ffffff;
            padding: 2em;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 600px;
            text-align: center;
        }

        /* Estilos del formulario */
        form {
            margin-top: 1em;
        }

        label {
            font-weight: 500;
        }

        input[type="text"] {
            width: 100%;
            padding: 0.8em;
            margin-top: 0.5em;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
        }

        button {
            background-color: #000;
            color: #fff;
            padding: 0.8em 1.2em;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 1em;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #333;
        }

        /* Estilos del resultado */
        .result {
            margin-top: 2em;
            padding: 1em;
            background-color: #f9fafb;
            border: 1px solid #ddd;
            border-radius: 8px;
            text-align: left;
        }

        .result p {
            margin: 0.5em 0;
        }

        .error {
            color: red;
            margin-top: 1em;
        }

        /* Estilos del contenedor del iframe */
        .iframe-container {
            margin-top: 2em;
            width: 100vw;
            height: 80vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        iframe {
            width: 100%;
            height: 100%;
            border: none;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <div class="container-form">
        <h2>Ingrese un enlace para obtener su IP y sus DNS</h2>
        <form method="post">
            <label for="url">URL:</label>
            <input type="text" id="url" name="url" required>
            <button type="submit">Obtener Información y Guardar</button>
        </form>
        <!-- Botón de salida -->
        <form action="https://www.google.com" method="get">
            <button type="submit">SALIR</button>
        </form>

        <?php if (isset($result)): ?>
            <div class="result">
                <h3>Información del enlace ingresado:</h3>
                <p><strong>URL:</strong> <?= htmlspecialchars($result["url"]) ?></p>
                <p><strong>IP:</strong> <?= htmlspecialchars($result["ip"]) ?></p>
                <p><strong>DNS:</strong> <?= htmlspecialchars($result["dns"]) ?></p>
            </div>
        <?php elseif (isset($error)): ?>
            <div class="error"><?= htmlspecialchars($error) ?></div>
        <?php endif; ?>
    </div>

    <!-- Contenedor para el iframe -->
    <div class="iframe-container">
        <?php if (isset($result)): ?>
            <iframe src="<?= htmlspecialchars($result["url"]) ?>" title="Página de <?= htmlspecialchars($result["url"]) ?>"></iframe>
        <?php endif; ?>
    </div>

    <!-- Script para deshabilitar clic derecho y teclas -->
    <script>
        // Deshabilitar el clic derecho
        document.addEventListener('contextmenu', event => event.preventDefault());

        // Deshabilitar teclas específicas
        document.addEventListener('keydown', function(event) {
            if (
    event.key === "F12" || // F12
    (event.ctrlKey && event.shiftKey && event.key.toLowerCase() === "i") || // Ctrl + Shift + I
    (event.ctrlKey && event.shiftKey && event.key.toLowerCase() === "j") || // Ctrl + Shift + J
    (event.ctrlKey && event.key.toLowerCase() === "u") || // Ctrl + U
    (event.ctrlKey && event.key.toLowerCase() === "s") // Ctrl + S
) {
    event.preventDefault();
}
        });
    </script>
</body>
</html>
