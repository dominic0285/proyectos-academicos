<?php
session_start();

// Usuario de demostración: demo / demo1234
// Genera tus propios hashes con: php -r "echo password_hash('tu_clave', PASSWORD_DEFAULT);"
$usuarios = [
    'demo' => '$2y$10$Ue5L92ku0oQM5PJSqjyUZebOw/8uO/SbJ9UEAJZqy4QelkhAeUBgq'
];

$usuario = $_POST['usuario'] ?? '';
$contrasena = $_POST['contrasena'] ?? '';

if (isset($usuarios[$usuario]) && password_verify($contrasena, $usuarios[$usuario])) {
    session_regenerate_id(true); // evita fijación de sesión
    $_SESSION['usuario'] = $usuario;
    header("Location: bienvenido.php");
    exit;
} else {
    http_response_code(401);
    echo "<h3>❌ Usuario o contraseña incorrectos</h3>";
    echo "<a href='index.php'>Volver</a>";
}
?>