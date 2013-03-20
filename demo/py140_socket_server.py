#/usr/bin/python
#socket_server.py

from socket import *
from time import ctime

def tcpServer():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', 8001))
    sock.listen(5)

    print 'waiting for connection...'

    while True:
        conn, addr = sock.accept()
        print '...connected from :', addr

        while True:
            buf = conn.recv(1024)
            print '[%s] %s' % (ctime(), buf)
            conn.send('[%s] %s' % (ctime(), buf))


if __name__ == '__main__':
    tcpServer()
