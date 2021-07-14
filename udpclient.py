#!/bin/python2.7

import argparse, socket

data = "AAABBBCCC" # Change this

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
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto(data, (target_host, target_port))

# receive some data
data, addr = client.recvfrom(4096)

print(data)
