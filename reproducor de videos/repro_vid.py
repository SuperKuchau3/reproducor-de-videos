import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import random
import pygame
import time
import threading


class ImagePlayer:
    def __init__(self, root, image_folder, music_folder):
        self.root = root
        self.image_folder = image_folder
        self.music_folder = music_folder
        self.images = self.load_images()
        self.music_files = self.load_music()
        self.current_index = random.randint(0, len(self.images) - 1)
        self.playing = False

        # Inicializa pygame para reproducir música
        pygame.init()
        pygame.mixer.init()

        # Label para mostrar la imagen
        self.label = tk.Label(root)
        self.label.pack()

        # Muestra la primera imagen de forma aleatoria
        self.show_image(self.current_index)

        # Botones de navegación
        btn_prev = tk.Button(root, text="Anterior", command=self.show_prev_image)
        btn_prev.pack(side=tk.LEFT, padx=20)

        btn_next = tk.Button(root, text="Siguiente", command=self.show_next_image)
        btn_next.pack(side=tk.RIGHT, padx=20)

        # Botones de reproducción automática
        btn_play = tk.Button(root, text="Reproducir", command=self.play_images)
        btn_play.pack(side=tk.LEFT, padx=20)

        btn_pause = tk.Button(root, text="Pausar", command=self.pause_images)
        btn_pause.pack(side=tk.RIGHT, padx=20)

        # Reproducción de videos
        self.video_label = tk.Label(root)
        self.video_label.pack()

    def load_images(self):
        """Carga las rutas de las imágenes desde la carpeta"""
        supported_formats = (".png", ".jpg", ".jpeg", ".bmp", ".gif")
        return [
            os.path.join(self.image_folder, file)
            for file in os.listdir(self.image_folder)
            if file.lower().endswith(supported_formats)
        ]

    def load_music(self):
        """Carga las rutas de los archivos de música desde la carpeta"""
        supported_formats = (".mp3", ".wav", ".ogg")
        return [
            os.path.join(self.music_folder, file)
            for file in os.listdir(self.music_folder)
            if file.lower().endswith(supported_formats)
        ]

    def show_image(self, index):
        """Muestra la imagen en el índice actual"""
        if not self.images:
            self.label.config(text="No hay imágenes en la carpeta")
            return
        image_path = self.images[index]
        image = Image.open(image_path)
        image = image.resize((500, 650), Image.Resampling.LANCZOS)  
        photo = ImageTk.PhotoImage(image)
        self.label.config(image=photo)
        self.label.image = photo

    def show_next_image(self):
        """Muestra la siguiente imagen"""
        if self.images:
            self.current_index = (self.current_index + 1) % len(self.images)
            self.show_image(self.current_index)

    def show_prev_image(self):
        """Muestra la imagen anterior"""
        if self.images:
            self.current_index = (self.current_index - 1) % len(self.images)
            self.show_image(self.current_index)

    def play_images(self):
        """Reproduce las imágenes de forma automática"""
        if not self.playing:
            self.playing = True
            self.play_music()
            self.show_next_image()
            self.root.after(5000, self.play_images)

    def pause_images(self):
        """Pausa la reproducción de imágenes"""
        self.playing = False

    def play_music(self):
        """Reproduce música de forma aleatoria"""
        if self.music_files:
            music_file = random.choice(self.music_files)
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play()


if __name__ == "__main__":
    # Crea la ventana principal
    root = tk.Tk()
    
    # Carpeta de imágenes
    image_folder = filedialog.askdirectory()
    
    # Carpeta de música
    music_folder = filedialog.askdirectory()
    
    # Inicia el reproductor de imágenes
    player = ImagePlayer(root, image_folder, music_folder)
    
    # Inicia el bucle principal
    root.mainloop()