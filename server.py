'''
Programmers: Ben Kocik, Parker Authier, Ava Zaremski
Project Description: Code for a device that provides illuminated directional information for building hallways
Code Description: Server to communicate to all clients or nodes.  Will also receive information from nodes.
'''

# Imports
import socket
import threading

'''
TODO:
1. Have main use a while loop to get door and emergency type from user
2. If there is a connection, create a new thread
3. When we want to send information, send same to all - will probably be easier
4. Implement protocol...
'''
# Appends to all messages - used mainly to bulk build messages
def add_to_messages(l, t):
    # l is the message list, t is the event type
    for m in range(len(l)):
        l[m] = l[m] + t
    return l

# Main function definition
def main():
    #########################
    ### Keys for protocol ###
    #########################
    # Sender/Receiver key
    SERVER = "00"
    NODEA = "01"
    NODEB = "02"
    NODEC = "03"
    # Event type key
    OFF = "00"
    FIRE = "01"
    TORNADO = "02"
    INTRUDER = "03"
    GENERAL = "04"
    HAPPY = "99"
    # Direction key
    FLASH = "0"
    LEFT = "1"
    RIGHT = "2"
    ARRIVE = "3"
    # Location key
    D1 = "01"
    D2 = "02"
    D3 = "03"
    D4 = "04"
    D5 = "05"
    D6 = "06"
    D7 = "07"
    #############################
    ### End keys for protocol ###
    #############################

    #TODO Start server

    # Get info from user, build message
    flag = True
    while flag:
        # Used to hold the message for the protocol
        messageA = "ALRT" + SERVER + NODEA  # Message from server to node A
        messageB = "ALRT" + SERVER + NODEB  # Message from server to node B
        messageC = "ALRT" + SERVER + NODEC  # Message from server to node C

        # List of all messages. Easier for appending same information
        messages = [messageA, messageB, messageC]

        # Welcome user
        print("Welcome")

        # Get event type from user
        print("Select an event to run")
        print("Options: Off (0), Fire (1), Tornado (2), Intruder (3), General Emergency (4), Happy Event (5)")
        event = int(input("Input event type: "))

        # Cases for events
        if event == 0 or (event < 0 or event > 5):
            close = input("Would you like to exit the server? (y/n) ")
            # If a user wants to turn it off, they can leave
            if "y" in close:
                flag = False
                # Turn off anyhow
                messages = add_to_messages(messages, OFF)
                messages = add_to_messages(messages, FLASH)     # Irrelevant - not needed
                messages = add_to_messages(messages, D1)        # Irrelevant - not needed
                #TODO Send message
                break
        elif event == 1:
            # Fire event
            messages = add_to_messages(messages, FIRE)
        elif event == 2:
            # Tornado event
            messages = add_to_messages(messages, TORNADO)
        elif event == 3:
            # Intruder event
            messages = add_to_messages(messages, INTRUDER)
        elif event == 4:
            # General emergency
            messages = add_to_messages(messages, GENERAL)
        elif event == 5:
            # Happy event
            messages = add_to_messages(messages, HAPPY)
        else:
            # This shouldn't happen, but if it does it will turn off
            messages = add_to_messages(messages, OFF)

        # Get door from user
        print("Select an exit door")
        print("Options: 1, 2, 3, 4, 5, 6, 7")
        # Door input must be between 1 and 7
        exitDoor = int(input("Input Door: "))

        # Handle sending info to correct node
        directionA = ""     # Node A
        directionB = ""     # Node B
        directionC = ""     # Node C
        location = ""       # Location for all

        # Cases for exit doors
        if exitDoor == 1:
            # Door 1: all left
            directionA = LEFT
            directionB = LEFT
            directionC = LEFT
            location = D1
        elif exitDoor == 2:
            # Door 2: node a arrive, node b and c left
            directionA = ARRIVE
            directionB = LEFT
            directionC = LEFT
            location = D2
        elif exitDoor == 3:
            # Door 3: node a right, node b and c left
            directionA = RIGHT
            directionB = LEFT
            directionC = LEFT
            location = D3
        elif exitDoor == 4:
            # Door 4: node a right, node b arrive, node c left
            directionA = RIGHT
            directionB = ARRIVE
            directionC = LEFT
            location = D4
        elif exitDoor == 5:
            # Door 5: node a and b right, node c left
            directionA = RIGHT
            directionB = RIGHT
            directionC = LEFT
            location = D5
        elif exitDoor == 6:
            # Door 6: node a and b right, node c arrive
            directionA = RIGHT
            directionB = RIGHT
            directionC = ARRIVE
            location = D6
        elif exitDoor == 7:
            # Door 7: all right
            directionA = RIGHT
            directionB = RIGHT
            directionC = RIGHT
            location = D7
        else:
            # This shouldn't happen, but if it does all will flash
            directionA = FLASH
            directionB = FLASH
            directionC = FLASH
            location = D1   # This is irrelevant, but may be needed

        # Append location to message
        messageA = messageA + directionA
        messageB = messageB + directionB
        messageC = messageC + directionC
        messages = [messageA, messageB, messageC]   # Remake list

        # Append location to all messages
        messages = add_to_messages(messages, location)

        ### DEBUGGING ###
        for m in messages:
            print(m)

        #TODO ensure at least one node is connected, send messages to all

        
'''
### PROTOCOL STUFF - TO BE DELETED ###

    # Create socket for server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")

    # Configure address and port
    PORT = 12345
    HOST = ""
    
    # Bind the port
    s.bind((HOST, PORT))
    print("Socket binded to port: " + str(PORT))

    s.listen(5)
    print("Socket is listening")

    while True:
        c, addr = s.accept()
        print("Received connection from " + str(addr))

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

        # Close if input is 0
        if exitDoor == 0:
            c.close()
        # Otherwise send door
        else:
            c.send(exitDoor)

'''

if __name__ == "__main__":
    main()