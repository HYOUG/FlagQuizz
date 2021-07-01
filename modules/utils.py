from time import strftime
from colorama import Fore, init

init(convert=True)

embed_color = 0x5865F2

def get_time():
    time = strftime("%H:%M:%S")
    return time


def red(text):
    colored_text = Fore.LIGHTRED_EX + text + Fore.RESET
    return colored_text


def blue(text):
    colored_text = Fore.LIGHTBLUE_EX + text + Fore.RESET
    return colored_text


def green(text):
    colored_text = Fore.LIGHTGREEN_EX + text + Fore.RESET
    return colored_text


def yellow(text):
    colored_text = Fore.LIGHTYELLOW_EX + text + Fore.RESET
    return colored_text


def pink(text):
    colored_text = Fore.LIGHTMAGENTA_EX + text + Fore.RESET
    return colored_text


def cyan(text):
    colored_text = Fore.LIGHTCYAN_EX + text + Fore.RESET
    return colored_text