from socket import *
server = ('localhost',12000)

clientSocket = socket(family = AF_INET, type = SOCK_DGRAM)
sentence = input('Input lowercase sentence:')
clientSocket.sendto(sentence.encode(),server)
modifiedSentence,addr = clientSocket.recvfrom(1024)
print ('From',addr,':', modifiedSentence.decode())
clientSocket.close()
