# Proyecto Login Seguro en PHP

Este proyecto es un sistema básico de login seguro en PHP usando sesiones y contraseñas hasheadas con `password_hash()` y verificación con `password_verify()`.

---

## Archivos incluidos

- `index.php`: Página inicial con formulario de login.
- `verificar.php`: Verifica usuario y contraseña.
- `bienvenido.php`: Página de bienvenida para usuarios autenticados.
- `logout.php`: Cierra sesión y redirige al login.

---

## Funcionalidades

- Control de sesión para usuarios autenticados.
- Almacenamiento seguro de contraseñas usando hashing bcrypt.
- Redirección automática si el usuario ya está logueado.
- Mensajes claros de error si las credenciales son incorrectas.
- Opción para cerrar sesión y volver a login.

---

## Cómo generar una nueva contraseña hasheada

Para crear una nueva contraseña hasheada que puedas agregar en el array `$usuarios` en `verificar.php`, usa este comando en tu terminal con PHP instalado:

```bash
php -r "echo password_hash('tu_clave_nueva', PASSWORD_BCRYPT) . PHP_EOL;"
```

Reemplaza `'tu_clave_nueva'` por la contraseña que quieras usar. Copia el resultado (el hash generado) y pégalo como valor en el array, por ejemplo:

```php
$usuarios = [
    'demo' => '$2y$10$tuHashGeneradoAqui...'
];
```

---

## Cómo ejecutar el proyecto localmente

1. Abre una terminal y navega a la carpeta donde están los archivos PHP.
2. Ejecuta el servidor embebido de PHP con el comando:

```bash
php -S localhost:8000
```

3. Abre tu navegador y entra a:

```
http://localhost:8000/index.php
```

4. Ingresa tu usuario y contraseña para probar el login.

---

## Notas

- Este proyecto es un ejemplo básico para aprender conceptos de seguridad en PHP.
- No uses este sistema en producción sin implementar más medidas de seguridad.
- Las contraseñas deben guardarse siempre con hashing y nunca en texto plano.

---


