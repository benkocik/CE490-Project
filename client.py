'''
Programmers: Ben Kocik, Parker Authier, Ava Zaremski
Project Description: Code for a device that provides illuminated directional information for building hallways
Code Description: Client code to receive information from server and other clients/nodes.
'''

# Imports
import socket

# Main function definition
def main():
    # Create socket
    s = socket.socket()

    # Configure port
    PORT = 12345
    ADDR = ""   #TODO figure out address of server

    # Connect to the server on computer
    s.connect((ADDR, PORT))

    # Get data from server
    data = s.recv(1024)

    #TODO: Decide on closing
    s.close
    

if __name__ == "__main__":
    main()