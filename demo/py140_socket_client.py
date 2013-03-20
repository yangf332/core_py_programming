#/usr/bin/python
#socket_client.py

from socket import *
from time import ctime

def tcpClient(ip, port):
    sock = socket.socket(AF_INET, SOCK_STREAM)
    sock.connect((ip, port))

    while True:
        data = raw_input('> ')
        sock.send(data)
        response = sock.recv(1024)
        print response


if __name__ == '__main__':
    tcpClient('127.0.0.1', 8001)

    