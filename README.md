# 🎓 Proyectos académicos y de práctica

Colección de proyectos que desarrollé mientras aprendía distintos lenguajes y conceptos: estructuras de datos, interfaces gráficas, procesamiento de señales, gráficos 3D, bots con IA y seguridad web.

| Proyecto | Lenguaje / Tecnologías | Descripción |
|---|---|---|
| [🤖 Tutor de matemáticas para Telegram](tutor-matematicas-telegram-bot) | Python · Telegram Bot API · Google Gemini | Bot que enseña operaciones básicas a niños con retroalimentación generada por IA y seguimiento de aciertos. |
| [📚 Biblioteca virtual](gestion-bibliotecaria-cpp) | C++ | Sistema de consola para gestionar libros digitales y físicos, préstamos, usuarios con aprobación de administrador y estadísticas. |
| [🧊 Cubo de Rubik 3D](cubo-rubik-3d-web) | JavaScript · Three.js | Simulación interactiva en 3D con rotación de filas/columnas y verificación de estado resuelto. |
| [📈 Visualizador de plano cartesiano](visualizador-plano-cartesiano) | Python · Tkinter · Matplotlib | Grafica coordenadas y genera una descripción automática de la tendencia (máximos, mínimos, dirección). |
| [🎙️ Grabadora de audio con STFT](grabadora-audio-stft) | Python · Librosa · SoundDevice | Graba audio, muestra la forma de onda, guarda su espectro (STFT) y reconstruye el audio a partir de él. |
| [🖼️ Imagen ⇄ texto](imagen-a-texto-gui) | Python · Tkinter · Pillow | Codifica una imagen en un archivo de texto (modo, tamaño y píxeles) y la reconstruye. |
| [🔐 Login seguro en PHP](login-seguro-php) | PHP | Autenticación con `password_hash`/`password_verify`, sesiones y regeneración de ID. |
| [🎲 Simulación Monte Carlo](simulacion-montecarlo) | Python · NumPy | Compara dos políticas de mantenimiento (costos, tiempos de retardo e inactividad) mediante simulación. |
| [🔤 Cifrado por sustitución](cifrado-sustitucion) | Python | Cifra y descifra texto con una tabla de símbolos reorganizada según una clave. |
| [🐍 Apps de escritorio en Python](python-interfaces-graficas) | Python · Tkinter · Matplotlib · Turtle | Gráficos de ventas y de torta, figuras interactivas y árbol fractal recursivo. |
| [🔗 Listas enlazadas](estructuras-de-datos) | Python · HTML | Listas enlazadas propias en consola y visualizadas en la web. |
| [🌐 PHP y web](php-y-web) | PHP · MySQL · JavaScript | Probador de cámara/micrófono, extractor de IP y DNS, corrector ortográfico, calculadora y gráficos Canvas. |

## 🚀 Cómo ejecutarlos

| Tipo | Cómo correrlo | Cómo empaquetarlo |
|---|---|---|
| Python con interfaz (Tkinter) | `pip install -r requirements.txt` (o las librerías del README) y `python archivo.py` | `pip install pyinstaller` → `pyinstaller --onefile --windowed archivo.py` → el `.exe` queda en `dist/` |
| Bot de Telegram | Copia `.env.example` a `.env`, pon tus claves y `python main.py` | Se despliega en un servidor gratis (Render, Railway o PythonAnywhere) |
| C++ | `g++ src/biblioteca_virtual.cpp -o biblioteca.exe` | El `.exe` ya es el ejecutable |
| PHP | `php -S localhost:8000` dentro de la carpeta | Cualquier hosting con PHP |
| Web (HTML/JS) | Abrir `index.html` | GitHub Pages |

## Autor

**Dominic De Freitas** — Ingeniero en Informática (UGMA). Desarrollo aplicaciones móviles y web con React Native, TypeScript, Node.js y Python, y busco mi primer puesto como desarrollador junior remoto.

[Perfil de GitHub](https://github.com/dominic0285) · [LinkedIn](https://www.linkedin.com/in/dominic-de-freitas-07102828a/) · dominicdefreitasfd@gmail.com
