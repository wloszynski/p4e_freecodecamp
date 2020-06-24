# Networked Programs

# library for TCP Sockets  
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80))

# mysock.connect( ('host', portNumber))

