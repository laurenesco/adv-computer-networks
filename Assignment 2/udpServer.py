from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM) # address family inet (ipv4), socket protocol UDP
serverSocket.bind(('', serverPort)) # Link object to a socket

print ("The server is ready to recieve")

while True:
		  message, clientAddress = serverSocket.recvfrom(2048) # Receive 2048 bit of data, this returns 2 parameters
		  modifiedMessage = message.decode().upper()
		  serverSocket.sendto(modifiedMessage.encode(), clientAddress)
