# Pygame Runner - WSL + VS Code Setup Guide

A step-by-step guide to getting your development environment ready for Pygame on WSL.

---

## Prerequisites

- Windows 10 (version 21H2+) or Windows 11
- Administrator access on your machine

---

## Step 1: Install WSL

Open **PowerShell as Administrator** and run:

```powershell
wsl --install
```

This installs WSL 2 with Ubuntu by default. Restart your computer when prompted.

After restarting, Ubuntu will launch automatically and ask you to create a username and password.

### Verify WSLg (GUI Support)

WSLg is included by default with WSL 2 on Windows 11 (and Windows 10 21H2+). It allows Linux GUI apps like Pygame windows to display on your desktop.

Verify it's working:

```bash
ls /mnt/wslg/
```

You should see files like `PulseServer`, `PulseAudioRDPSink`, etc. If this directory doesn't exist, update WSL:

```powershell
# Run in Windows PowerShell (not WSL)
wsl --update
```

---

## Step 2: Install VS Code + WSL Extension

1. Download and install [VS Code](https://code.visualstudio.com/) on Windows
2. Install the **WSL** extension (by Microsoft) from the Extensions sidebar (`Ctrl+Shift+X`, search "WSL")
3. Open a WSL terminal in VS Code:
   - Press `Ctrl+Shift+P` > type "WSL: New Window" > select it
   - Or open a terminal and type `wsl` to enter your Linux environment

You should see **WSL: Ubuntu** in the bottom-left corner of VS Code.

---

## Step 3: Install Python and pip

Ubuntu usually comes with Python pre-installed. Verify:

```bash
python3 --version
```

If it's not installed:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
```

---

## Step 4: Install Pygame

```bash
pip3 install pygame
```

Or if you prefer using a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
pip install pygame
```

Verify the install:

```bash
python3 -c "import pygame; print(pygame.ver)"
```

You should see something like `2.6.1`.

---

## Step 5: Install Audio Support (PulseAudio)

WSLg provides a PulseAudio server for audio, but the client library needs to be installed in your Linux environment:

```bash
sudo apt install -y libpulse0
```

This allows Pygame's mixer to play sound effects and music through your Windows speakers.

---

## Step 6: Create Your Project Folder

```bash
mkdir -p ~/Dev/pygame-runner
cd ~/Dev/pygame-runner
```

Open it in VS Code:

```bash
code .
```

You're ready to start building! Head over to the **TEACHING_GUIDE.md** to build the game step by step.

---

## Troubleshooting

### Window doesn't appear / app hangs

WSLg's display server may need a reset. In **Windows PowerShell**:

```powershell
wsl --shutdown
```

Then reopen VS Code / WSL and try again.

### `pygame.error: mixer not initialized` or `dsp: No such audio device`

Pygame needs to be told to use PulseAudio through WSLg. Add these lines at the top of your script, **before** `pygame.init()`:

```python
import os
os.environ['SDL_AUDIODRIVER'] = 'pulseaudio'
os.environ['PULSE_SERVER'] = 'unix:/mnt/wslg/PulseServer'
```

### `pygame.error: Failed loading libpulse-simple.so.0`

Install the PulseAudio client library:

```bash
sudo apt install -y libpulse0
```

### `FileNotFoundError` for images or sounds

1. Make sure you `cd` into the project directory before running your script — the game uses relative paths
2. Linux is **case-sensitive** — `Fly1.png` and `fly1.png` are different files. Make sure filenames in your code match the actual files exactly

### `ModuleNotFoundError: No module named 'pygame'`

```bash
pip3 install pygame
```

If using a virtual environment, make sure it's activated (`source venv/bin/activate`).
