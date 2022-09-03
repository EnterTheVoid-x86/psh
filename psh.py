import sys
import os
import socket
import platform
from config import *
# psh v2.1, rsh ported to python
# created by etvx86

try:    
    if sys.argv[1] == "--no-logo":
        ascii = "disabled"
    elif sys.argv[1] == "--info":
        print("psh v2.1, rsh ported to python")
        print("created by etvx86")
        sys.exit()
    elif sys.argv[1] == "--version":
        print("psh v2.1")
        sys.exit()
    elif sys.argv[1] == "--debug":
        debug = True
    elif sys.argv[1] == "--help":
        print("psh v2.1 command arguments")
        print("--no-logo: disable the logo")
        print("--info: print info about psh")
        print("--version: print the psh version")
        print("--debug: enable debug mode")
        sys.exit()
except IndexError:
    pass

if platform.system() == "Windows":
    print("Error: psh cannot be run on Windows!")
    exit()

asciilogo = open("ascii.txt")
asciiart = asciilogo.read()

CBLACK = '\33[30m'
CRED = '\33[31m'
CGREEN = '\33[32m'
CYELLOW = '\33[33m'
CBLUE = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE = '\33[36m'
CWHITE = '\33[37m'

if debug == True:
    print("Debug mode enabled")
    print("Greeting: " + greeting)
    print("Prompt: " + prompt)
    print("Ascii: " + ascii)
    print("Python version: " + platform.python_version())
    print("Getting username...")
    print("Username: " + os.getlogin())
    print("Getting hostname...")
    print("Hostname: " + socket.gethostname())
    print("Getting system...")
    print("System: " + platform.system())
    print("[!] PROMPT MAIN CREATION")
    print("[!] INIT COLORS")
    print("[!] INIT PROMPT")

if ascii == "enabled":
    print(asciiart)
print(greeting)

username = os.getlogin()
hostname = socket.gethostname()
def main():
    try:
        while True:
            directory = os.getcwd()
            shell = input(CBLUE + username + CGREEN + "<@>" +
                  CYELLOW + hostname + CWHITE + "%" + directory + prompt)
            sharray = shell.split(" ")
            if "exit" in sharray[0]:
                print("Exiting...")
                sys.exit()
            elif "help" in sharray[0]:
                try:
                    if sharray[1] == "autocomplete":
                        print("autocomplete v1.0.0")
                        print(CWHITE + "A psh built-in command to find a command based on user input.")
                        print("USAGE: Run the command. You will be asked to input a few letters that are included in the command. It will find commands that have your input in them.")
                        main()
                    elif sharray[1] == "sysinfo":
                        print("sysinfo v2.1")
                        print(CWHITE + "A psh built-in command to display system information.")
                        print("USAGE: Run the command.")
                        main()
                    elif sharray[1] == "pcalc":
                        print("pcalc v1.3")
                        print(CWHITE + "A psh built-in command to do simple calculations.")
                        print("USAGE: Run the command and type in a problem. The shell will do the math for you.")
                        main()
                    elif sharray[1] == "help":
                        print("I dont think you need help on this one.")
                        main()
                except IndexError:
                    print("psh help:")
                    print("Generally speaking, all you need to know is you can use any commands available to you in any other shell like nano.")
                    print("psh built in commands:")
                    print("autocomplete - find commands based on user input")
                    print("sysinfo - print system information")
                    print("pcalc - simple calculator")
                    print("help - print this help screen")
                    print("exit - exit psh")
            elif "sysinfo" in sharray[0]:
                print("psh v2.1")
                print("Running on " + platform.platform())
            elif "pcalc" in sharray[0]:
                print("Type exit to exit.")
                while True:
                    calc = input(">> ")
                    if calc == "exit":
                        break
                    else:
                        print(eval(calc))
            elif "autocomplete" in sharray[0]:
                print("Type in the start of some commands, we will find a command with that string included.")
                while True:
                    autoinput = input(">> ")
                    if autoinput == "exit":
                        break
                    else:
                        os.system("ls /usr/bin/ | grep " + autoinput)
            elif "cd" in sharray[0]:
                try:
                    os.chdir(sharray[1])
                except FileNotFoundError:
                    print("Invalid directory.")
                except IndexError:
                    print("Please input a directory.")
            else:
                os.system(shell)
    except KeyboardInterrupt:
        print("")
        main()
    except EOFError:
        print("\nExiting...")
        sys.exit()
main()
