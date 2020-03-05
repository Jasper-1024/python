from socket import *

if __name__ == "__main__":
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    print("ready receive")
    while True:
        message, clientAdress = serverSocket.recvfrom((2048))
        modifiedMessage = message.decode().upper()
        serverSocket.sendto(modifiedMessage.encode(), clientAdress)