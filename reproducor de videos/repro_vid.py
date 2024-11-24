import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImagePlayer:
    def __init__(self, root, image_folder):
        self.root = root
        self.image_folder = image_folder
        self.images = self.load_images()
        self.current_index = 0

        # Label para mostrar la imagen
        self.label = tk.Label(root)
        self.label.pack()

        # Muestra la primera imagen
        self.show_image(self.current_index)

        # Botones de navegación
        btn_prev = tk.Button(root, text="Anterior", command=self.show_prev_image)
        btn_prev.pack(side=tk.LEFT, padx=20)

        btn_next = tk.Button(root, text="Siguiente", command=self.show_next_image)
        btn_next.pack(side=tk.RIGHT, padx=20)

    def load_images(self):
        """Carga las rutas de las imágenes desde la carpeta"""
        supported_formats = (".png", ".jpg", ".jpeg", ".bmp", ".gif")
        return [
            os.path.join(self.image_folder, file)
            for file in os.listdir(self.image_folder)
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


if __name__ == "__main__":
    # Crea la ventana principal
    root = tk.Tk()
    
    # Carpeta de imágenes
    image_folder = filedialog.askdirectory()
    
    # Inicia el reproductor de imágenes
    player = ImagePlayer(root, image_folder)
    
    # Inicia el bucle principal
    root.mainloop()
