#!/usr/bin/python3

# William
# this program opens a specific port

import socket

def open_port(port_number):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', port_number))
    s.listen(1)
    while True:
        print("Listening on port", port_number)
        c, addr=s.accept()
        print("Connection from", addr)
        print("Closing")
        s.close()
        break
    s.exit()

if __name__=="__main__":
    open_port(10000)




