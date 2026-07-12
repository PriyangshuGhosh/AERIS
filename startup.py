import importlib
import platform
import sys

from banner import print_banner
from utils.helpers import internet_available


REQUIRED_PACKAGES = [

    "fastapi",

    "uvicorn",

    "llama_cpp",

    "huggingface_hub",

    "dotenv",

    "psutil",

    "colorama"

]


def check_python():

    print("[1/5] Checking Python Version...")

    if sys.version_info < (3, 10):

        raise RuntimeError(
            "Python 3.10 or newer is required."
        )

    print(f"      OK ({platform.python_version()})")


def check_dependencies():

    print("\n[2/5] Checking Dependencies...\n")

    for pkg in REQUIRED_PACKAGES:

        try:

            importlib.import_module(pkg)

            print(f"✓ {pkg}")

        except Exception:

            raise RuntimeError(
                f"Missing dependency: {pkg}"
            )


def check_network():

    print("\n[3/5] Checking Internet...")

    if internet_available():

        print("✓ Connected")

    else:

        print("⚠ Offline Mode")

        print("Model must already exist in cache.")


def startup_checks():

    print_banner()

    check_python()

    check_dependencies()

    check_network()

    print()