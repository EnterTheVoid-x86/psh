# psh v1.2, rsh ported to python
# created by etvx86
import os
import time
import socket
import platform
import sys

if sys.argv[1] == "--uninstall":
	uninst = input("Are you sure? (y/n)")
	if uninst == "y":
		print("Uninstalling...")
		if platform.system() == "Windows":
			os.system("del psh.py")
		else:
			os.system("rm psh.py")
		print("Uninstall completed.")
print("Welcome to psh, the open-source shell made in python.")

username = os.getlogin()
hostname = socket.gethostname()
while True:
		shell = input(username + "@" + hostname + "~$ ")
		if shell == "exit":
			print("Exiting...")
			exit()
		elif shell == "help":
			print("psh help:")
			print("Depending on the OS, any unix or Windows commands are supported.")
			print("psh built in commands:")
			print("sysinfo - print system information")
			print("help - print this help screen")
			print("exit - exit psh")
		elif shell == "sysinfo":
			print("psh v1.2")
			print("Running on " + platform.system())
		else:
			os.system(shell)