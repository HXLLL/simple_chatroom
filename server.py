import values
import socket
import servant
import logging
import threading

clients = []

if __name__ == "__main__":
    #init
    logging.basicConfig(level=logging.INFO)
    server_addr = sys.argv[1]
    server_port = eval(sys.argv[2])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((server_addr, server_port))
    sock.listen(8)

    #conn,client_addr = sock.accept()
    #servant.serve(conn,client_addr)

    try:
        while True:
            conn,client_addr = sock.accept()
            clients.append(conn)
            t = threading.Thread(target=servant.handle_client, args=(conn,client_addr,clients))
            t.start()
    except KeyboardInterrupt:
        pass