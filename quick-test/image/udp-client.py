#!/usr/bin/python
import socket
import os
udp_port = int(os.environ['UDP_PORT'])
udp_server_ip = os.environ['UDP_SERVER_IP']

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = (udp_server_ip, udp_port)
bufferSize          = 1024 

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
 
# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0])
print(msg)
