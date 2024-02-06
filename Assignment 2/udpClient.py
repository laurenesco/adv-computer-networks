from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Input a lowercase sentence: ")

# sendto() is for UDP, send() is TCP
clientSocket.sendto(message.encode(), (serverName, serverPort)) # what are you sending, and where

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print (modifiedMessage.decode())

clientSocket.close()
