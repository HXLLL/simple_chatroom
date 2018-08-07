import threading
import time
import os,signal
import logging
import values
import re

data = threading.local()

def remove(client):
    global clients
    if client in clients:
        clients.remove(client)

def broadcast(content):
    print(content)
    global clients
    for client in clients:
        try:
            client.send(content.encode('utf-8'))
        except:
            client.close()
            if client in clients:
                clients.remove(client)
        

def execute(cmd):
    cmds = re.split(r'\s+', cmd)
    logging.info("  client:%s  command: %s" % (data.name, cmd))
    if cmds[0] == 'exit':
        broadcast("%s disconnected" % data.name)
        raise BaseException('Client Disconnected')
    elif cmds[0] == 'name':
        newname = cmds[1]
        broadcast("%s changed its name to %s" % (data.name, newname))
        data.name = newname
    

def handle_client(conn, addr, _clients):
    data.name = addr[0]
    global clients
    clients = _clients
    try:
        while True:
            time.sleep(0.03)
            message = conn.recv(values.SIZE)
            if not message:
                continue
            if message[0] == b'/'[0]:
                try:
                    execute(message[1:].decode('utf-8'))
                except BaseException as err:
                    print(err)
                    break
            else:
                broadcast("%s: %s" % (data.name, message.decode('utf-8')))
    except ConnectionResetError:
        conn.close()
        broadcast("%s disconnected" % data.name)