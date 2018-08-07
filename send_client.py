import socket
import time

if __name__ == "__main__":
    #init
    server_addr = 'localhost'
    server_port = 8305

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_addr, server_port))

    while True:
        message = input()
        sock.send(message.encode('utf-8'))
        if message == '/exit':
            break