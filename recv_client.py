import values
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
        message = sock.recv(values.SIZE)
        print(message.decode('utf-8'))