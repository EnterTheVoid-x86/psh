# psh v1.2, rsh ported to python
# created by etvx86
import platform, socket, os, sys

from config import *

asciilogo = open("ascii.txt")
asciiart = asciilogo.read()

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

if ascii == "enabled":
	print(asciiart)
print(greeting)

username = os.getlogin()
hostname = socket.gethostname()
while True:
		shell = input(CBLUE + username + "@" + CYELLOW + hostname + CWHITE + prompt)
		if shell == "exit":
			print("Exiting...")
			sys.exit()
		elif shell == "help":
			print("psh help:")
			print("Depending on the OS, any unix or Windows commands are supported.")
			print("psh built in commands:")
			print("sysinfo - print system information")
			print("pcalc - simple calculator")
			print("help - print this help screen")
			print("exit - exit psh")
		elif shell == "sysinfo":
			print("psh v1.2")
			print("Running on " + platform.system())
		elif shell == "pcalc":
			print("Type exit to exit.")
			while True:
				calc = input(">> ")
				if calc == "exit":
					break
				else:
					print(eval(calc))
		else:
			os.system(shell)