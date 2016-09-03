import socket
import sys


HOST = 'localhost'
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall(sys.argv[1])

while True:
    data = s.recv(1024)
    if data:
        print data
    else:
        break

s.close()
