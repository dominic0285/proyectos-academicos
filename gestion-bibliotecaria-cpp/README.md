# 📚 Proyecto Atlas — Biblioteca virtual en C++

Aplicación de consola para **gestionar una biblioteca**: libros digitales (PDF) y físicos, préstamos con fecha de entrega y usuarios con aprobación de administrador. Todo se guarda en archivos de texto.

## ✨ Funcionalidades

- **Administrador** (usuario `admin`): registrar libros digitales y físicos, ver registros y libros prestados.
- **Usuario**: consultar el catálogo, abrir un libro digital por su código y solicitar préstamos de libros físicos (calcula día de salida y de entrega).
- Persistencia en archivos `.txt` con `ofstream` / `ifstream`.
- Interfaz de consola con menús y colores.

## 🗂️ Estructura

```
src/
  biblioteca_virtual.cpp        Programa principal
  modulos/
    aprobacion_usuarios.cpp     Registro de usuarios con aprobación del administrador
    registro_usuario.cpp        Alta de usuarios
    grafico_estadisticas.cpp    Gráfico de estadísticas en consola
    fecha_y_hora.cpp            Manejo de fechas con <ctime>
libros/                         Coloca aquí los PDF (nombre = código del libro, ej. 1234.pdf)
archivo generado.txt            Catálogo de ejemplo
```

## 🚀 Compilar y ejecutar (Windows)

```bash
g++ src/biblioteca_virtual.cpp -o biblioteca.exe
biblioteca.exe
```

> Usa `windows.h` / `conio.h` y comandos de consola de Windows (`cls`, `color`, `start`).

## 👤 Autor

**Dominic De Freitas** — [GitHub](https://github.com/dominic0285)
