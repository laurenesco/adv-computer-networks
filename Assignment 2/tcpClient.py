from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
cleintSocket.connect((serverName, serverPort)) # Knock on the door

message = input("Input a lowercase sentence: ")

# sendto() is for UDP, send() is TCP
clientSocket.send(message.encode()) # what are you sending

modifiedMessage = clientSocket.recv(2048)

print (modifiedMessage.decode())

clientSocket.close()
