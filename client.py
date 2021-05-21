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
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Configure port
    PORT = 12345
    HOST = "192.168.1.114"   #TODO figure out address of server

    # Connect to the server on computer
    s.connect((HOST, PORT))

    # Get data from server
    data = s.recv(1024)
    print(str(data))

    #TODO: Decide on closing
    s.close
    

if __name__ == "__main__":
    main()