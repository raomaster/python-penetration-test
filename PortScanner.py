#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)


host = '137.74.187.104'
port = 443

def portScanner(port):
    if s.connect_ex(host, port):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)