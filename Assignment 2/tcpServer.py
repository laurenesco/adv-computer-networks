from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) # address family inet (ipv4), protocol TCP
serverSocket.bind(('', serverPort)) # Link object to a socket

serverSocket.listen(1) # how many clients you will listen to at a time

print ("The server is ready to recieve")

while True:
		  connectionSocket, address = serverSocket.accept() # return connection socket and client address
		  print (address)

# recv for tcp, recvfrom for udp
message = connectionSocket.recv(2048).decode() # Receive 2048 bit of data, this returns 2 parameters
modifiedMessage = message.upper()
connectionSocket.send(modifiedMessage.encode())

connectionSocket.close()
