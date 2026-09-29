
<?php
session_start();

// Verificar si está logueado
if (!isset($_SESSION['usuario'])) {
    header("Location: index.php");
    exit;
}

echo "<h2>Bienvenido, " . htmlspecialchars($_SESSION['usuario']) . "!</h2>";
echo "<a href='logout.php'>Cerrar sesión</a>";
?>
