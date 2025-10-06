import tkinter as tk

# Main intro text (shown just once at startup)
INTRO_TEXT = (
    "Life Stocks 2001 DOS Terminal - Available Commands:\n\n"
    "Type 'help' at any time to list DOS commands!\n"
)

# Short help text (shown by help command)
HELP_TEXT = (
    "help          Show this help message\n"
    "dir           List files and directories\n"
    "date          Display the system date and time\n"
    "ver           Show system version info\n"
    "cls           Clear the screen\n"
    "echo <text>   Display text\n"
    "type <file>   Display contents of a file\n"
    "cd <folder>   Change current directory (experimental)\n"
    "win           Start LifeStocks OS\n"
    "exit          Quit the emulator\n"
    "run <app>     Launch an application or game\n"
)

def show_terminal(parent_frame, on_os_load=None):
    prompt = "C:\\> "
    terminal = tk.Text(parent_frame, bg="#000", fg="#0f0", font=("Courier", 16),
                       height=30, width=85, insertbackground="#0f0",
                       borderwidth=0, highlightthickness=0)
    terminal.pack(expand=True, fill="both")
    terminal.config(state="normal")

    # Insert intro and prompt
    terminal.insert(tk.END, INTRO_TEXT)
    terminal.insert(tk.END, prompt)
    terminal.mark_set("input_start", tk.END)
    terminal.focus_set()

    def handle_command(event=None):
        print("DEBUG: handle_command called")
        
        # Debug: Check mark positions
        input_start_pos = terminal.index("input_start")
        end_pos = terminal.index(tk.END)
        print(f"DEBUG: input_start position: {input_start_pos}")
        print(f"DEBUG: END position: {end_pos}")
        
        # Get current line content
        current_line = terminal.get("input_start", tk.END)
        print(f"DEBUG: Current line: '{repr(current_line)}'")
        
        # Try getting the last line instead
        last_line = terminal.get("end-1l linestart", "end-1c")
        print(f"DEBUG: Last line: '{repr(last_line)}'")
        
        # Extract command from the last line (remove prompt)
        if last_line.startswith(prompt):
            command = last_line[len(prompt):].strip()
        else:
            command = current_line.strip()
        
        print(f"DEBUG: Processed command: '{command}'")
        
        if not command:
            print("DEBUG: Empty command, adding new prompt")
            terminal.insert(tk.END, "\n" + prompt)
            terminal.mark_set("input_start", tk.END)
            terminal.see(tk.END)
            return "break"
        
        output = ""
        if command.lower() == "help":
            output = HELP_TEXT
            print("DEBUG: Help command matched")
        elif command.lower() == "dir":
            output = "Directory listing:\n AUTOEXEC.BAT\n CONFIG.SYS\n COMMAND.COM"
        elif command.lower() == "date":
            import datetime
            output = f"Current date is {datetime.datetime.now().strftime('%a %m/%d/%Y')}"
        elif command.lower() == "ver":
            output = "LifeStocks DOS Version 2.01"
        elif command.lower() == "cls":
            terminal.delete(1.0, tk.END)
            terminal.insert(tk.END, prompt)
            terminal.mark_set("input_start", tk.END)
            return "break"
        elif command.lower().startswith("echo "):
            output = command[5:]  # Remove "echo " prefix
        elif command.lower() == "win":
            if on_os_load:
                on_os_load()
            return "break"
        elif command.lower() == "exit":
            print("DEBUG: Exit command matched - closing application")
            # Find the root window and close it
            root = terminal.winfo_toplevel()
            root.quit()
            root.destroy()
            return "break"
        else:
            output = f"'{command}' is not recognized as an internal or external command"
            print("DEBUG: Unknown command")
        
        print(f"DEBUG: Adding output: '{output[:50]}...'")
        print(f"DEBUG: Output length: {len(output)}")
        
        # Add output and new prompt
        terminal.config(state="normal")  # Ensure terminal is editable
        terminal.insert(tk.END, "\n" + output + "\n" + prompt)
        terminal.mark_set("input_start", tk.END)
        terminal.see(tk.END)
        terminal.update()  # Force update of the display
        print("DEBUG: Text inserted and display updated")
        return "break"

    def on_key_press(event):
        # Handle Enter key specially
        if event.keysym == "Return":
            return handle_command(event)
        
        # Allow all other keys to be processed normally
        return None

    terminal.bind("<Key>", on_key_press)

    return terminal
