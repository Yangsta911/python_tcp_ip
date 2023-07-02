import socket
import sys
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

sock.listen(1)
return_data = '{"id": 8001}'
send_data = json.loads(return_data)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data == "8000":
                print >>sys.stderr, 'sending data back to the client: %s' %send_data["id"]
                connection.sendall(str(send_data["id"]))
            
    finally:
        # Clean up the connection
        connection.close()