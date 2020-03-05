#!/usr/bin/python3
from socket import *

if __name__ == "__main__":
    serverName = '172.17.0.2'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = input('input lowrcase sentence')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAdress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
    clientSocket.close()
