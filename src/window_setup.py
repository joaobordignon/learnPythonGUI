import tkinter as tk
from PIL import Image, ImageTk
import os

def create_main_window(background_path, window_title="Retro Computer Simulator"):
    root = tk.Tk()
    root.title(window_title)

    img = Image.open(background_path)
    photo = ImageTk.PhotoImage(img)
    width, height = img.size
    root.geometry(f"{width}x{height}")

    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=photo, anchor="nw")
    canvas.bg_photo = photo  # Prevent GC

    return root, canvas
