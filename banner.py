import os
import platform
import psutil
import socket

from colorama import Fore, Style, init

init(autoreset=True)


def print_banner():

    print()

    print(Fore.CYAN + "=" * 65)

    print(
        Fore.GREEN +
        "              GAAC AI LOCAL PHI SERVER v1.0"
    )

    print(Fore.CYAN + "=" * 65)

    print()

    print(
        f"{Fore.YELLOW}Operating System : "
        f"{platform.system()} {platform.release()}"
    )

    print(
        f"{Fore.YELLOW}Python Version   : "
        f"{platform.python_version()}"
    )

    print(
        f"{Fore.YELLOW}CPU              : "
        f"{platform.processor()}"
    )

    print(
        f"{Fore.YELLOW}CPU Cores        : "
        f"{os.cpu_count()}"
    )

    print(
        f"{Fore.YELLOW}RAM              : "
        f"{round(psutil.virtual_memory().total/(1024**3),2)} GB"
    )

    print(
        f"{Fore.YELLOW}Hostname         : "
        f"{socket.gethostname()}"
    )

    print()

    print(Fore.CYAN + "=" * 65)

    print(Style.RESET_ALL)