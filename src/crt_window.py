# src/crt_window.py

import tkinter as tk

# Constants for CRT geometry
CRT_X1, CRT_Y1 = 435, 115 
CRT_X2, CRT_Y2 = 1410, 880

def create_crt_frame(root):
    """
    Creates and places the CRT monitor region Frame on the given Tk root window.
    Returns: (frame, width, height)
    """
    crt_width = CRT_X2 - CRT_X1
    crt_height = CRT_Y2 - CRT_Y1
    frame = tk.Frame(root, width=crt_width, height=crt_height, bg="#000", bd=0, highlightthickness=0)
    frame.place(x=CRT_X1, y=CRT_Y1)
    frame.pack_propagate(False)
    return frame, crt_width, crt_height
