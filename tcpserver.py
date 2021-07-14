import argparse
import socket
import threading

# create parser object
parser = argparse.ArgumentParser()

# add parser arguments
parser.add_argument('BIND_IP', type=str)
parser.add_argument('BIND_PORT', type=int)

# parse arguments
args = parser.parse_args()

# assign arguments to variables
bind_ip = args.BIND_IP
bind_port = args.BIND_PORT

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))

# this is our client-handling thread
def handle_client(client_socket):

    # print out what the client sends
    request = client_socket.recv(1024)

    print("[*] Received: %s" % request)

    # send back a packet
    client_socket.send("ACK!")

    client_socket.close()

while True:

    client, addr = server.accept()

    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))

    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
