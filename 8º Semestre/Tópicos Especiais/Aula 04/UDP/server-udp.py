#!/usr/bin/env python3
import socket

localIP       = "127.0.0.1"
localPort     = 20001
bufferSize    = 1024
msgFromServer = "Hello World"
bytesToSend   = str.encode(msgFromServer)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

print("Servidor rodando")

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Mensagem do Cliente:{}".format(message)
    clientIP  = "IP do Cliente:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

    UDPServerSocket.sendto(bytesToSend, address)