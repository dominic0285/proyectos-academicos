# Gráfica Interactiva en Plano Cartesiano

Este proyecto es una aplicación de escritorio desarrollada en Python usando `Tkinter` y `Matplotlib`, que permite ingresar coordenadas manualmente para graficarlas en un plano cartesiano. Además, genera una descripción automática de la gráfica con palabras resaltadas como la tendencia, punto de inicio, máximo y mínimo.

## Características

- Interfaz gráfica amigable con campos para ingresar valores del eje X e Y.
- Gráfica generada en tiempo real con puntos de inicio y fin destacados.
- Descripción automática que interpreta la tendencia (ascendente, descendente o estable).
- Resaltado visual en el texto de análisis.
- Uso de `matplotlib` para graficar dentro de una ventana `tkinter`.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `matplotlib`
  - `tkinter` (incluida por defecto en la mayoría de las instalaciones de Python)

Puedes instalar matplotlib con:

```bash
pip install matplotlib
```

## Uso

Ejecuta el archivo Python y aparecerá una ventana donde podrás:

1. Ingresar 4 puntos para el eje X y eje Y.
2. Presionar el botón **Actualizar Gráfica** para ver el resultado.
3. Leer una descripción automatizada de la gráfica con los valores clave.

---

**Autor:** Dominic de Freitas
