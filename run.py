import os
import platform
import shutil
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
print("GAAC AI Local Phi Server")
print("=" * 60)

# -------------------------------------------------
# Create virtual environment
# -------------------------------------------------

if not os.path.exists(VENV):

    print("\nCreating virtual environment...\n")

    subprocess.check_call([
        sys.executable,
        "-m",
        "venv",
        VENV
    ])

# -------------------------------------------------
# Install requirements (only first time)
# -------------------------------------------------

marker = os.path.join(VENV, ".installed")

if not os.path.exists(marker):

    print("\nInstalling dependencies...\n")

    subprocess.check_call([
        PYTHON,
        "-m",
        "pip",
        "install",
        "--upgrade",
        "pip"
    ])

    subprocess.check_call([
        PIP,
        "install",
        "-r",
        "requirements.txt"
    ])

    open(marker, "w").close()

# -------------------------------------------------
# Create .env
# -------------------------------------------------

if not os.path.exists(".env"):

    if os.path.exists(".env.example"):

        shutil.copy(".env.example", ".env")

        print(".env created.")

# -------------------------------------------------
# Start Server
# -------------------------------------------------

print("\nLaunching server...\n")

subprocess.call([PYTHON, "server.py"])