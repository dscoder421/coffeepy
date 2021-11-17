import os
from colorama import init, Fore, Back, Style
from ddos import ddos
from portscan import portscan
from sqlinject import sqlinject

init()

def functionEnd():
    ans = input(Fore.GREEN + "Command finished.. Do you want to continue: ")
    if ans == "y":
        os.system("cls")
        main()
    else:
        exit()

#  ______
# |______|
# |__||__|
# |__||__|
# |__||__|

def main():
    os.system("cls")
    print("""
"""+ Fore.GREEN + """CofeePy by Dereck Smith """ + Fore.RESET + """

     ) ) )
    ( ( ( 
   |     |---
   | Cof |   |
   | ee! |   |
   |_____|---

Made in pure python.

This software is made for fun, if the author has more time, even hacking tools but now there is only useful tools. Enjoy

Choose your function:
""" + Fore.CYAN + """
1) Website IP Address
2) SQL Injection
3) DDOS Attack
    """)
    cmd = input(Fore.GREEN + ">>> ")
    if cmd == "1":
        # Find Port
        print(Fore.GREEN + "$ Port scanner chosen. Executing" + Fore.RESET)
        portscan.scan()
        functionEnd()
    elif cmd == "2":
        # SQL Injection
        sqlinject.injectMenu()
        functionEnd()
    elif cmd == "3":
        ddos.ddos_menu()
        functionEnd()
    else:
        os.system("cls")
        print(Fore.RED + "Error: Unknown command..")
        main()

main()