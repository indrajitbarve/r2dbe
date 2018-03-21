#!/usr/bin/env python
import socket
import sys

SRV_DEFAULT_HOST="localhost"
SRV_DEFAULT_PORT=1973
SRV_MAX_MSGLEN=256

if __name__ == "__main__":
	# initialize socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# send each line on stdin
	for ln in sys.stdin.readlines():
		snd_size = sock.sendto(ln.strip(),(socket.gethostbyname(SRV_DEFAULT_HOST),SRV_DEFAULT_PORT))
		if snd_size < 0:
			sys.stderr.write("Send to {sock} failed".format((socket.gethostbyname(SRV_DEFAULT_HOST),SRV_DEFAULT_PORT)))

