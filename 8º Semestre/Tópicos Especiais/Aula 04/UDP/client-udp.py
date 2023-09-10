#!/usr/bin/env python3
import socket

msgFromClient     = "Hello World"
bytesToSend       = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 20001)
bufferSize        = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Mensagem do servidor: {}".format(msgFromServer[0])

print(msg)