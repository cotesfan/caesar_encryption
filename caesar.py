# Script created by @cotesfan :)
from colorama import Fore
import os

# <------------ VARIABLES ------------>

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
encrypted_word = []
positions = []
new_positions = []

lblue = Fore.LIGHTBLUE_EX
lgreen = Fore.LIGHTGREEN_EX
lred = Fore.LIGHTRED_EX
lmagenta = Fore.LIGHTMAGENTA_EX
lcyan = Fore.LIGHTCYAN_EX
white = Fore.LIGHTWHITE_EX
reset = Fore.RESET  


banner = f"""{lgreen}
 ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗     ███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗    ██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██║     ███████║█████╗  ███████╗███████║██████╔╝    █████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║
██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗    ██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║
╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║    ███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   ██║╚██████╔╝██║ ╚████║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
         {lmagenta}By @cotesfan     



        {lcyan}     {white} ► {lcyan} 1. Encrypt\n             {white} ► {lcyan} 2.Decrypt (13 default)\n             {white} ► {lcyan} 99. Exit      {reset}  

"""
# <------------ MAIN ------------>

def encrypt():


    while True:

        try:

            positions = []
            new_positions = []
            letters = []
            w = str(input(f"{lmagenta}Word:{white} "))
            word = w.lower()
            displace = int(input((f"{lmagenta}Number of displaced words: {white}")))

            for i in word:
                letters.append(i)
                position = alphabet.index(i)
                positions.append(position)

            for x in positions:

                new_position = x + displace
                if new_position > 25:
                    rest = new_position - 25
                    new_position = 0 + rest
                new_positions.append(new_position)
        
            os.system("clear")
            print(f"{lgreen}[+] Encrypted word: {white}", end="")
            for z in new_positions:

                print(alphabet[z], end="")

            print(f"{lred}\n99. Menu")

            opc = int(input("> "))

            if opc == 99:
                menu()
            else:
                print("Opcion invalida")    
        
        except KeyboardInterrupt:

            print(f"{lred}Ctrl + C...")
            break

        except ValueError:

            break

def decrypt():

    while True:

        try:

            positions = []
            new_positions = []
            letters = []

            w = str(input(f"{lmagenta}Word: {white}"))
            word = w.lower()

            for i in word:
                
                letters.append(i)
                position = alphabet.index(i)
                positions.append(position)


            for x in positions:
                new_position = x - 13
                if new_position < 0:
                    new_position += 26
                new_positions.append(new_position)

            os.system("clear")
            print(f"{lred}[-] Decrypted word: {white}", end="")
            for z in new_positions:
                print(alphabet[z], end="")     


            print(f"{lred}\n99. Menu")

            opc = int(input("> "))

            if opc == 99:
                menu()
            else:
                print("Opcion invalida")

        except KeyboardInterrupt:

            print(f"{lred}Ctrl + C...")
            break

        except ValueError:

            break


def menu():

    while True:
        
        try:

            print(banner)
            opt = int(input("> "))
            
            if opt == 1:
                encrypt()

            elif opt == 2:
                decrypt()

            elif opt == 99:
                break

            else:
                print(f"{lred}[!] Invalid option{reset}")
                break

        except KeyboardInterrupt:

            print(f"{lred}Ctr + C...{reset}")
            break

        except ValueError:

            break
        


menu()



