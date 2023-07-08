import socket
import sys
import json
import time
import threading
from time import sleep

def alive_check():
    data_alive = '{"id": 8000}'
    send_alive = json.loads(data_alive)

    while True:
        # Send data
        print >>sys.stderr, 'sending "%s"\n' % send_alive["id"]
        sock.sendall(str(send_alive["id"]))
        return_data = sock.recv(16)
        if return_data == "8001":
            print >>sys.stderr, 'received "%s"\n' % return_data  
        time.sleep(15)


def handshake():
    data_handshake = '{"id": 8001}'
    send_handshake = json.loads(data_handshake)

    while True:
        # Send data
        print >>sys.stderr, 'sending "%s\n"' % send_handshake["id"]
        sock.sendall(str(send_handshake["id"]))
        return_data = sock.recv(16)
        if return_data == "8101":
            print >>sys.stderr, 'received "%s"' % return_data  
        time.sleep(20)


if __name__ =="__main__":
        # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print >>sys.stderr, 'connecting to %s port %s\n' % server_address
    sock.connect(server_address)
    # creating thread
    delay = 5
    t1 = threading.Thread(target=alive_check)
    sleep(delay)
    t2 = threading.Thread(target=handshake)
 
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

