'''
Programmers: Ben Kocik, Parker Authier, Ava Zaremski
Project Description: Code for a device that provides illuminated directional information for building hallways
Code Description: Server to communicate to all clients or nodes.  Will also receive information from nodes.
'''

# Imports
import socket

# Main function definition
def main():

    # Create socket for server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")

    # Configure address and port
    PORT = 12345
    
    # Bind the port
    s.bind(('', PORT))
    print("Socket binded to port: " + str(PORT))

    s.listen(5)
    print("Socket is listening")

    while True:
        c, addr = s.accept()
        print("Received connection from " + str(addr))
        
        c.send("Thanks for connecting")
        '''
        # Get door from user
        print("Select an exit door")
        print("Options: 1, 2, 3, 4, 5, 6, 7")
        exitDoor = 0
        # Door input must be between 1 and 7
        while exitDoor < 1 and exitDoor > 7:
            exitDoor = input("Input Door (must be between 1 and 7): ")
        
        # Get emergency type from user
        #TODO: Talk to client

        #TODO: Send information to client
        c.send(exitDoor)
        '''
    #TODO: Decide on closing
    c.close()

if __name__ == "__main__":
    main()