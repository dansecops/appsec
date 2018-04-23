#!/usr/bin/python
import socket
import sys

# Iterate over each IP
for ip in range(1, 254):
    try:
        # Create a Socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the Server
        connect = s.connect(('10.11.1.' + str(ip), 25))
        # Receive the banner
        banner = s.recv(1024)
        # VRFY a user
        s.send('VRFY root\r\n')
        result = s.recv(1024)
        # Check if server replies to the VRFY command (user known=250, user unknown=550)
        if "250" in result or "550" in result:
            print('10.11.1.' + str(ip) + ' responded to SMTP VRFY command')
        # Close the socket
        s.close()
    except:
        print('10.11.1.' + str(ip) + ' not reachable')

