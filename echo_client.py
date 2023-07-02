import socket
import sys
import json
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)


send_data = '{"id": 8000}'
data = json.loads(send_data)

while True:
    # Send data
    print >>sys.stderr, 'sending "%s"' % data["id"]
    sock.sendall(str(data["id"]))
    return_data = sock.recv(16)
    print >>sys.stderr, 'received "%s"' % return_data  
    time.sleep(15)

