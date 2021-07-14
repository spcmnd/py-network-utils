#!/bin/python2.7

import argparse, socket

data = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"

# create parser object
parser = argparse.ArgumentParser()

# add parser arguments
parser.add_argument('TARGET_HOST', type=str)
parser.add_argument('TARGET_PORT', type=int)

# parse arguments
args = parser.parse_args()

# assign arguments to variables
target_host = args.TARGET_HOST
target_port = args.TARGET_PORT

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send(data)

# receive some data
response = client.recv(4096)

print(response)
