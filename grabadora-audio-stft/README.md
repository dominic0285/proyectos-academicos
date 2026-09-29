# Audio a Texto - Grabadora y Reconstrucción de Audio

Este proyecto es una aplicación de escritorio desarrollada en Python con `tkinter`, `sounddevice`, `librosa` y `matplotlib` que permite:

- Grabar audio desde el micrófono.
- Visualizar en tiempo real la forma de onda.
- Guardar la grabación y su representación espectral usando STFT (Transformada de Fourier de Tiempo Corto).
- Reconstruir el audio a partir de las características almacenadas (magnitud y fase).

### 🧠 ¿Cómo funciona?

El sistema tiene dos pestañas principales:

- **Grabar**:
  - Permite iniciar y detener una grabación de audio.
  - Muestra la forma de onda en tiempo real.
  - Guarda:
    - El archivo `.wav` del audio original.
    - Un archivo `.npz` con la magnitud y fase del espectrograma generado mediante STFT.

- **Reconstruir**:
  - Permite seleccionar un archivo `.npz` generado anteriormente.
  - Reconstruye el audio a partir de los datos y lo guarda como un nuevo `.wav`.

### 💡 Tecnologías utilizadas

- Python 3.x
- Tkinter (interfaz gráfica)
- SoundDevice (captura de audio)
- Librosa (procesamiento de audio)
- SoundFile (guardar archivos de audio)
- Numpy
- Matplotlib

### 📦 Instalación

1. Asegúrate de tener Python 3.x instalado.
2. Instala las dependencias necesarias:

```bash
pip install sounddevice librosa soundfile matplotlib
```

3. Ejecuta el script:

```bash
python nombre_del_archivo.py
```

### 👨‍💻 Autor

Dominic de Freitas

---

¡Gracias por visitar este repositorio!