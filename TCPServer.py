#!/usr/bin/python3

import socket

#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

#Binding to socket
serversocket.bind((host, port)) #Host will be replaced with the IP, if changed and not running on host

#Starting TCP listener
serversocket.listen(3)

while True:
    #Starting the connection
    clientsocket, address = serversocket.accept()

    print("receive connection from %s " % str(address))
    message = 'Hello! Thank you for connecting to the server' + "\r\n"
    
    #Response to client
    clientsocket.send(message.encode(ascii))

    clientsocket.close()

