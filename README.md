# 🖥️ LifeStocks Energy Systems - Retro Computer Simulator

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![Status](https://img.shields.io/badge/Status-In%20Development-orange.svg)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)

> *Experience computing like it's 1985! A nostalgic journey through retro technology with authentic BIOS boot sequences, DOS terminal emulation, and classic GUI interfaces.*

## 🎮 What is LifeStocks Energy Systems?

Step back in time to the golden age of personal computing! This project recreates the authentic experience of booting up a vintage computer system from the 1980s-90s, complete with:

- **Realistic BIOS Boot Sequence** - Watch memory tests count up, hardware detection, and system initialization
- **Authentic DOS Terminal** - Command-line interface with period-appropriate commands
- **Retro GUI Environment** - Classic windowed interface reminiscent of early operating systems
- **CRT Monitor Simulation** - Curved screen effects and green phosphor glow

## 🚀 Features

### ✨ Current Features
- **🖥️ Authentic Boot Experience**
  - Award BIOS v4.51PG simulation
  - Animated memory test (0K → 4096K)
  - Hardware detection sequences
  - Company branding and splash screens

- **💻 DOS Terminal Emulator**
  - Classic green-on-black display
  - Working command prompt (C:\>)
  - Built-in help system
  - Multiple DOS commands supported

- **🎨 Retro Aesthetics**
  - CRT monitor frame simulation
  - Period-appropriate fonts (Courier)
  - Authentic color schemes
  - Nostalgic sound effects (planned)

### 📋 Available DOS Commands
```
help          Show available commands
dir           List files and directories  
date          Display system date and time
ver           Show system version info
cls           Clear the screen
echo <text>   Display text
type <file>   Display file contents
cd <folder>   Change directory
win           Launch graphical OS
exit          Quit the emulator
run <app>     Launch applications
```

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- Tkinter (usually included with Python)
- PIL/Pillow for image handling

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/joaobordignon/learnPythonGUI.git
   cd learnPythonGUI
   ```

2. **Install dependencies**
   ```bash
   pip install pillow
   ```

3. **Run the simulator**
   ```bash
   python src/main.py
   ```

## 🎯 Project Structure

```
learnPythonGUI/
├── src/
│   ├── main.py              # Main application entry point
│   ├── boot_sequence.py     # BIOS/POST boot simulation
│   ├── terminal.py          # DOS command terminal
│   ├── window_setup.py      # Main window configuration
│   └── crt_window.py        # CRT monitor frame simulation
├── assets/
│   └── images/
│       └── background/
│           └── gameBackground.png
└── README.md
```

## 🗺️ Roadmap

### 🔄 Phase 1: Core Terminal (✅ Complete)
- [x] Basic boot sequence
- [x] DOS terminal emulator
- [x] Command processing system
- [x] Help system implementation

### 🎨 Phase 2: Enhanced Experience (🚧 In Progress)
- [ ] Sound effects (startup beeps, key clicks)
- [ ] More realistic CRT effects (scanlines, curvature)
- [ ] Additional DOS commands and utilities
- [ ] File system simulation

### 🖱️ Phase 3: Graphical Environment (📅 Planned)
- [ ] Window manager implementation
- [ ] Desktop environment with icons
- [ ] File manager application
- [ ] Text editor application
- [ ] Simple games (Solitaire, Minesweeper)

### 🎮 Phase 4: Interactive Applications (📅 Future)
- [ ] Programming environment/IDE
- [ ] Retro games collection
- [ ] Network simulation tools
- [ ] System utilities and diagnostics

### 🌐 Phase 5: Advanced Features (💭 Vision)
- [ ] Multiple computer models to choose from
- [ ] Save/load system states
- [ ] User customizable hardware configurations
- [ ] Educational mode with explanations

## 🎮 How to Use

1. **Start the Application**
   - Run `python src/main.py`
   - Watch the authentic BIOS boot sequence

2. **Use the DOS Terminal**
   - Type `help` to see available commands
   - Try commands like `dir`, `date`, or `ver`
   - Use `cls` to clear the screen

3. **Launch GUI Mode**
   - Type `win` to start the graphical interface
   - Use `exit` to quit the application

## 🤝 Contributing

We welcome contributions! Whether you're interested in:
- 🐛 Bug fixes and improvements
- ✨ New features and commands
- 🎨 Visual enhancements and effects
- 📚 Documentation improvements
- 🎵 Sound effects and audio

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and test thoroughly
4. Commit with descriptive messages
5. Push to your branch and create a Pull Request

## 📸 Screenshots

*Coming soon! Screenshots of the boot sequence, terminal, and GUI environment will be added as features are completed.*

## 🎯 Educational Value

This project serves as an excellent learning resource for:
- **Python GUI Development** with Tkinter
- **Event-driven Programming** concepts
- **Retro Computing History** and appreciation
- **User Interface Design** principles
- **Software Architecture** patterns

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by classic computers from the 1980s-90s
- Award Software BIOS for reference materials
- The retro computing community for preservation efforts
- All contributors who help bring this nostalgic experience to life

## 💬 Contact

- **Project Link**: [https://github.com/joaobordignon/learnPythonGUI.git](https://github.com/joaobordignon/learnPythonGUI.git)
- **Issues**: Report bugs and request features in the GitHub Issues section
- **Discussions**: Join conversations in the GitHub Discussions tab

---

*⚡ Powered by nostalgia and green phosphor displays ⚡*

**Experience the magic of retro computing - one boot sequence at a time!** 🖥️✨