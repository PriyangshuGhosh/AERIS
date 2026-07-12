import os
import platform
import subprocess
import sys

VENV = "venv"

WINDOWS = platform.system() == "Windows"

if WINDOWS:
    PYTHON = os.path.join(VENV, "Scripts", "python.exe")
    PIP = os.path.join(VENV, "Scripts", "pip.exe")
else:
    PYTHON = os.path.join(VENV, "bin", "python")
    PIP = os.path.join(VENV, "bin", "pip")

print("=" * 60)
print("GAAC AI Local Phi Server Installer")
print("=" * 60)

# Create virtual environment
if not os.path.exists(VENV):
    print("\nCreating virtual environment...")
    subprocess.check_call([sys.executable, "-m", "venv", VENV])

# Upgrade pip
print("\nUpgrading pip...")
subprocess.check_call([PYTHON, "-m", "pip", "install", "--upgrade", "pip"])

# Install requirements
print("\nInstalling dependencies...")
subprocess.check_call([PIP, "install", "-r", "requirements.txt"])

# Copy .env if needed
if not os.path.exists(".env") and os.path.exists(".env.example"):
    import shutil
    shutil.copy(".env.example", ".env")
    print("\nCreated .env from .env.example")

print("\nStarting server...\n")

subprocess.call([PYTHON, "server.py"])