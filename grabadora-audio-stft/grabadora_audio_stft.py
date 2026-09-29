import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sounddevice as sd
import librosa
import soundfile as sf
import numpy as np
import os
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AudioApp:
    def __init__(self, master):
        self.master = master
        master.title("Procesamiento de Audio")
        self.sr = 22050  # Tasa de muestreo
        self.is_recording = False
        self.audio_data = []  # Se acumulan los datos de audio aquí
        self.setup_ui()

    def setup_ui(self):
        # Crear pestañas
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill="both", expand=True)

        self.tab_record = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_record, text="Grabar")

        self.tab_reconstruct = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_reconstruct, text="Reconstruir")

        # Pestaña de Grabación
        self.record_button = tk.Button(self.tab_record, text="Iniciar Grabación", command=self.toggle_recording,
                                       bg="green", fg="white", font=("Arial", 12))
        self.record_button.pack(pady=10)

        self.entry_filename = ttk.Entry(self.tab_record, width=30)
        self.entry_filename.insert(0, "nombre_grabacion")
        self.entry_filename.pack(pady=5)

        # Área para visualización en tiempo real de la forma de onda
        self.figure, self.ax = plt.subplots(figsize=(5, 2))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.tab_record)
        self.canvas.get_tk_widget().pack()

        # Pestaña de Reconstrucción
        self.btn_load_features = ttk.Button(self.tab_reconstruct, text="Cargar Grabación", command=self.load_features)
        self.btn_load_features.pack(pady=10)

        self.file_listbox = tk.Listbox(self.tab_reconstruct)
        self.file_listbox.pack(pady=5, fill="both", expand=True)

        self.reconstruct_button = ttk.Button(self.tab_reconstruct, text="Reconstruir Audio", command=self.reconstruct_audio)
        self.reconstruct_button.pack(pady=10)

        self.update_file_list()

    def toggle_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.record_button.config(text="Grabando...", bg="red")
            self.audio_data = []  # Reiniciar datos
            threading.Thread(target=self.record_audio, daemon=True).start()
            self.start_plot_update()  # Inicia actualización periódica de la gráfica
        else:
            self.is_recording = False
            self.record_button.config(text="Iniciar Grabación", bg="green")

    def record_audio(self):
        # Abre el stream de entrada y acumula los datos mientras esté grabando
        with sd.InputStream(samplerate=self.sr, channels=1, callback=self.audio_callback):
            while self.is_recording:
                sd.sleep(100)
        # Al finalizar la grabación, guarda el audio y las características
        self.save_audio()

    def audio_callback(self, indata, frames, time, status):
        # Acumula los datos de audio; no se actualiza la gráfica aquí para evitar conflictos de hilos
        self.audio_data.extend(indata[:, 0])

    def start_plot_update(self):
        # Actualiza la gráfica cada 200 ms mientras se graba
        if self.is_recording:
            self.update_plot()
            self.master.after(200, self.start_plot_update)

    def update_plot(self):
        self.ax.clear()
        # Muestra los últimos 1000 puntos para la visualización de la forma de onda
        if len(self.audio_data) > 0:
            data_to_plot = self.audio_data[-1000:]
            self.ax.plot(data_to_plot)
        self.canvas.draw()

    def save_audio(self):
        filename = self.entry_filename.get().strip()
        if not filename:
            messagebox.showerror("Error", "Debe ingresar un nombre para la grabación.")
            return

        audio_array = np.array(self.audio_data)
        # Guardar el audio original en WAV
        sf.write(f"{filename}.wav", audio_array, self.sr)

        # Usar parámetros por defecto de librosa para STFT/ISTFT
        n_fft = 2048   # Parámetro por defecto de librosa.stft
        hop_length = 512  # Valor por defecto

        stft = librosa.stft(audio_array, n_fft=n_fft, hop_length=hop_length)

        # Guardar la magnitud, fase y parámetros en un archivo NPZ
        features = {
            "magnitude": np.abs(stft),
            "phase": np.angle(stft),
            "n_fft": n_fft,
            "hop_length": hop_length
        }
        np.savez(f"{filename}_features.npz", **features)
        messagebox.showinfo("Guardado", f"Grabación guardada como {filename}.wav y {filename}_features.npz")
        self.update_file_list()

    def update_file_list(self):
        self.file_listbox.delete(0, tk.END)
        for file in os.listdir():
            if file.endswith("_features.npz"):
                self.file_listbox.insert(tk.END, file)

    def load_features(self):
        selected = self.file_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Seleccione una grabación para reconstruir.")
            return
        self.selected_file = self.file_listbox.get(selected[0])
        messagebox.showinfo("Seleccionado", f"Archivo seleccionado: {self.selected_file}")

    def reconstruct_audio(self):
        if not hasattr(self, "selected_file"):
            messagebox.showerror("Error", "Seleccione un archivo primero.")
            return
        try:
            data = np.load(self.selected_file)
            magnitude = data["magnitude"]
            phase = data["phase"]
            n_fft = int(data["n_fft"]) if "n_fft" in data.files else 2048
            hop_length = int(data["hop_length"]) if "hop_length" in data.files else 512
            stft = magnitude * np.exp(1j * phase)
            y_inv = librosa.istft(stft, hop_length=hop_length)
            output_filename = self.selected_file.replace("_features.npz", "_reconstructed.wav")
            sf.write(output_filename, y_inv, self.sr)
            messagebox.showinfo("Reconstrucción", f"Audio reconstruido guardado en {output_filename}")
        except Exception as e:
            messagebox.showerror("Error al reconstruir audio", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioApp(root)
    root.mainloop()
