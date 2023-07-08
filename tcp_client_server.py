import socket
import sys
import json
import threading

def alive_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 10000)
    print >>sys.stderr, 'starting up on %s port %s\n' % server_address
    sock.bind(server_address)

    sock.listen(1)
    return_alive = '{"id": 8001}'
    send_alive = json.loads(return_alive)

    while True:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection\n'
        connection, client_address = sock.accept()

        try:
            print >>sys.stderr, 'connection from', client_address

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print >>sys.stderr, 'received "%s"' % data
                if data == "8000":
                    print >>sys.stderr, 'sending data back to the client: %s' %send_alive["id"]
                    connection.sendall(str(send_alive["id"]))
                
        finally:
            # Clean up the connection
            connection.close()

def handshake_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 10001)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)

    sock.listen(1)
    return_handshake = '{"id":8101}'
    send_handshake = json.loads(return_handshake)

    while True:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection\n'
        connection, client_address = sock.accept()

        try:
            print >>sys.stderr, 'connection from', client_address

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print >>sys.stderr, 'received "%s"' % data
                if data == "8001":
                    print >>sys.stderr, 'sending data back to the client: %s' %send_handshake["id"]
                    connection.sendall(str(send_handshake_handshake["id"]))
                
        finally:
            # Clean up the connection
            connection.close()



if __name__ =="__main__":
    # creating thread
    t1 = threading.Thread(target=alive_server)
    t2 = threading.Thread(target=handshake_server)
 
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()