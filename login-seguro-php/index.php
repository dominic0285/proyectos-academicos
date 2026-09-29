
<?php
session_start();

// Redirección si ya está logueado
if (isset($_SESSION['usuario'])) {
    header("Location: welcome.php");
    exit;
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Seguro</title>
</head>
<body>
    <h2>Login</h2>

    <form action="verificar.php" method="POST">
        <label for="usuario">Usuario:</label>
        <input type="text" id="usuario" name="usuario" required><br><br>

        <label for="contrasena">Contraseña:</label>
        <input type="password" id="contrasena" name="contrasena" required><br><br>

        <button type="submit">Ingresar</button>
    </form>
</body>
</html>
