import socket
import time
import sys

if __name__ == "__main__":
    #init
    server_addr = sys.argv[1]
    server_port = eval(sys.argv[2])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_addr, server_port))

    while True:
        message = input()
        sock.send(message.encode('utf-8'))
        if message == '/exit':
            break