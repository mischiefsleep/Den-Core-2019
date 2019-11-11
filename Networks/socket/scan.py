#!/usr/bin/python3

# Guilhem Mizrahi 09/2019

# This program takes a hostname (IPv4 address of hostname such as localhost etc...) and will scan the ports on this host
# A better port scanner would use connect_ex because it doesn't require

import socket # This package allows to manipulate ports and manage connections

def check_port(hostname, port):
    '''
    This function will try to connect to the port on the specified hostname and return True if it managed to do so (indicating that the port is open) otherwise it will return False (indicating that the port is closed)
    '''
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates the socket from which the program will try to connect (think of it as one end of the connection) the arguments specify that the socket uses IPv4 and tcp
    connect=s.connect_ex((hostname, port)) # connect_ex returns 0 if it managed to connect of something else if it didn't
    s.close() # Don't forget to close the socket otherwise the program will not continue
    return(connect==0) # Returns True if it managed to connect, False otherwise

def main(hostname, low_port=1, high_port=65535):
    '''
    This function call the scanner check_port on the host hostname for each port ranging from low_port to high_port (both included)
    It will print the list of opened ports
    By default it will scan for all possible ports
    '''
    print("Starting the scan on", hostname, "from port", low_port, "to", high_port)
    empty=True # This variable is used to check if all the ports are closed
    for port_number in range(low_port, high_port+1): # The +1 makes it so that the last port will also be scanned
        if check_port(hostname, port_number): # If the port is opened
            print("Port", str(port_number).rjust(5), "is opened") # Print it to the screen
            empty=False # The all_closed variable is set to false, meaning that at least one port is opened
    if empty:
        print("No port opened") # If all ports are closed then the empty variable has remained True and the program will print to the screen

if __name__=="__main__":
    print("Hostname is ", socket.gethostname()) # This line make is easier to see the localhost hostname (even though local host will work too, or 127.0.0.1)
    hostname=input("Type a hostname or IP address\n") # Prompt the user for a hostname or an IP address
    main(hostname) # Call the main function
    print("Scan complete")
