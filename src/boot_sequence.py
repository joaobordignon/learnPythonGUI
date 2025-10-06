import tkinter as tk
import time

# ASCII Art Logo for LifeStocks Energy Systems
ENERGY_LOGO = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                          LIFESTOCKS ENERGY SYSTEMS                           ║
║                               BIOS Version 2.01                              ║
║                          Copyright 1985-2001 LES Inc.                        ║
╚══════════════════════════════════════════════════════════════════════════════╝

"""

# Initial BIOS/POST lines
BOOT_LINES_PART1 = [
    "Award Modular BIOS v4.51PG, An Energy Star Ally",
    "Copyright (C) 1984-2001, Award Software, Inc.",
    "",
    "LIFESTOCKS ENERGY SYSTEMS - Model LES-2001",
    "Main Processor: Intel 80486DX2-66 MHz",
    "Math Coprocessor: Built-in",
    "BIOS Date: 10/06/01",
    "",
    "Base Memory: 640K",
    "Extended Memory: 3072K",
    "",
    "Performing Memory Test..."
]

# Lines after memory test
BOOT_LINES_PART2 = [
    "",
    "Memory Test Complete - 4096K OK",
    "",
    "Detecting Hardware:",
    "  Primary IDE Controller... Found",
    "  Secondary IDE Controller... Found", 
    "  Floppy Drive Controller... Found",
    "  Parallel Port (LPT1)... Found at 0378h",
    "  Serial Port (COM1)... Found at 03F8h",
    "  Serial Port (COM2)... Found at 02F8h",
    "",
    "Keyboard Controller... OK",
    "Mouse... OK",
    "",
    "Boot Sequence: A:, C:",
    "Searching for Boot Record from Floppy... Not Found",
    "Searching for Boot Record from Hard Disk... Found",
    "",
    "Loading MS-DOS...",
    "",
    "Starting LifeStocks DOS v2.01..."
]

def show_boot_sequence(parent, on_end=None, lines=None, delay=800):
    """
    Animates a realistic POST/BIOS boot sequence with animated memory test.
    Calls `on_end()` when done (for switching to terminal or next screen).
    """
    widget = tk.Text(parent, bg="#000", fg="#00ff00", font=("Courier", 12),
                      height=30, width=85, borderwidth=0, highlightthickness=0, 
                      insertbackground="#00ff00", wrap=tk.NONE)
    widget.pack(expand=True, fill="both")
    widget.config(state="disabled")

    def show_logo():
        """Display the company logo first"""
        widget.config(state="normal")
        widget.insert(tk.END, ENERGY_LOGO)
        widget.config(state="disabled")
        widget.see(tk.END)
        widget.after(2000, show_part1)  # Show logo for 2 seconds

    def show_part1():
        """Show initial BIOS lines"""
        widget.config(state="normal")
        for line in BOOT_LINES_PART1:
            widget.insert(tk.END, line + "\n")
        widget.config(state="disabled")
        widget.see(tk.END)
        widget.after(1000, animate_memory_test)  # Wait 1 second before memory test

    def animate_memory_test():
        """Animate the memory test counting up"""
        memory_values = [0, 256, 512, 768, 1024, 1280, 1536, 1792, 2048, 2304, 2560, 2816, 3072, 3328, 3584, 3840, 4096]
        
        def update_memory(i=0):
            if i < len(memory_values):
                # Clear the last line and show new memory value
                widget.config(state="normal")
                if i > 0:
                    # Remove the last line
                    widget.delete("end-2l", "end-1l")
                
                # Add current memory test line
                widget.insert(tk.END, f"Testing Memory: {memory_values[i]}K\n")
                widget.config(state="disabled")
                widget.see(tk.END)
                
                # Continue with next value after short delay
                widget.after(150, update_memory, i + 1)
            else:
                # Memory test complete, show part 2
                widget.after(500, show_part2)
        
        update_memory()

    def show_part2():
        """Show the rest of the boot sequence"""
        widget.config(state="normal")
        
        def next_line(i=0):
            if i < len(BOOT_LINES_PART2):
                widget.insert(tk.END, BOOT_LINES_PART2[i] + "\n")
                widget.see(tk.END)
                
                # Variable delays for more realistic feel
                if "Loading" in BOOT_LINES_PART2[i] or "Starting" in BOOT_LINES_PART2[i]:
                    delay_time = 1500  # Longer delay for loading messages
                elif BOOT_LINES_PART2[i].strip() == "":
                    delay_time = 200   # Short delay for empty lines
                else:
                    delay_time = 600   # Normal delay
                
                widget.after(delay_time, next_line, i + 1)
            else:
                widget.config(state="disabled")
                if callable(on_end):
                    widget.after(1000, on_end)  # Wait 1 second before calling on_end
        
        next_line()

    # Start the sequence with the logo
    show_logo()
    return widget
