import tkinter as tk
from PIL import Image, ImageTk
import os
# Local imports
from window_setup import create_main_window
from crt_window import create_crt_frame
from boot_sequence import show_boot_sequence
from terminal import show_terminal
# Constants
BACKGROUND_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "images", "background", "gameBackground.png")


def main():
    root, canvas = create_main_window(BACKGROUND_PATH)
    frame, crt_width, crt_height = create_crt_frame(root)

    def launch_os():
        # This function will be called when the user types 'win'
        # Here you could destroy/clear the terminal and launch a new GUI, dialogue, etc.
        # For now, just display a message
        for widget in frame.winfo_children():
            widget.destroy()
        import tkinter as tk
        label = tk.Label(frame, text="Graphical OS booted! (Placeholder)", fg="white", bg="#123", font=("Courier", 20))
        label.pack(expand=True, fill="both")

    def after_boot():
        # Remove boot widget (everything in frame), then launch terminal
        for widget in frame.winfo_children():
            widget.destroy()
        show_terminal(frame, on_os_load=launch_os)
    
    # Start with boot sequence; after it's finished, show terminal
    show_boot_sequence(frame, on_end=after_boot)

    root.mainloop()

if __name__ == "__main__":
    main()

