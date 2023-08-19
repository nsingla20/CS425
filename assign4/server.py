from socket import *
server = ('localhost',12000)

serverSocket = socket(family = AF_INET, type = SOCK_DGRAM)
serverSocket.bind(server)
print ("The server is ready to receive")

while True:
    name, addr = serverSocket.recvfrom(1024)
    print("Connection from", addr, "is established")
    sentence = name.decode()
    capitalizedSentence = sentence.upper()
    serverSocket.sendto(capitalizedSentence.encode(),addr)

