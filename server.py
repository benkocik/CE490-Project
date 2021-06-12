'''
Programmers: Ben Kocik, Parker Authier, Ava Zaremski
Project Description: Code for a device that provides illuminated directional information for building hallways
Code Description: Server to communicate to all clients or nodes.  Will also receive information from nodes.
'''

# Imports
import socket
import threading

# Appends to all messages - used mainly to bulk build messages
def add_to_messages(l, t):
    # l is the message list, t is the event type
    for m in range(len(l)):
        l[m] = l[m] + t
    return l 

# Listens to messages being send from any node
def receive_msg_thread(c, node):
    while True:
        # Receive data
        rawData = c.recv(1024)
        data = rawData.decode('utf-8')

        # Parse messages from data
        messageType = data[0:4]
        sender = data[4:6]
        receiver = data[6:8]
        powerSource = data[8:9]
        batt = data[9:12]
        # Support for any length of message, check for no message
        if data[11] != data[-1]:
            errorMsg = data[12:-1] + data[-1]
        else:
            errorMsg = ""

        # Print message
        if messageType == "RECV":
            if node == "01":
                print("\n\nNode A says:")
            elif node == "02":
                print("\n\nNode B says:")
            elif node == "03":
                print("\n\nNode C says:")
            else:
                print("Unknown node says:")
            if powerSource == "0":
                print("Power source: Battery")
                print("Battery percentage " + batt)
            elif powerSource == "1":
                print("Power source: Wall")
            else:
                print("Error retreiving power source")
            print(errorMsg)

# Main function definition
def main():
    # Welcome user
    print("Welcome")

    # IP Address Key
    AADDR = "169.254.29.196"
    BADDR = "169.254.197.118"
    CADDR = "169.254.115.119"
    # Debugging
    #AADDR = "192.168.1.101"
    #BADDR = "192.168.1.126"
    #CADDR = "192.168.1.118"

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

    # Create socket for server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")

    # Configure address and port
    PORT = 12345
    HOST = ""

    # Bind the port
    s.bind((HOST, PORT))
    print("Socket binded to port: " + str(PORT))
    
    print("Waiting for all clients to connect...")
    s.listen(5)

    # Accept 3 connections
    c1, addr1 = s.accept()
    c2, addr2 = s.accept()
    c3, addr3 = s.accept()

    # Define threads to receive messages from client
    # NODE A
    if addr1[0] == AADDR:
        t1 = threading.Thread(target=receive_msg_thread, args=(c1, NODEA))
    elif addr2[0] == AADDR:
        t1 = threading.Thread(target=receive_msg_thread, args=(c2, NODEA))
    elif addr3[0] == AADDR:
        t1 = threading.Thread(target=receive_msg_thread, args=(c3, NODEA))

    # NODE B
    if addr1[0] == BADDR:
        t2 = threading.Thread(target=receive_msg_thread, args=(c1, NODEB))
    elif addr2[0] == BADDR:
        t2 = threading.Thread(target=receive_msg_thread, args=(c2, NODEB))
    elif addr3[0] == BADDR:
        t2 = threading.Thread(target=receive_msg_thread, args=(c3, NODEB))
    
    # NODE C
    if addr1[0] == CADDR:
        t3 = threading.Thread(target=receive_msg_thread, args=(c1, NODEC))
    elif addr2[0] == CADDR:
        t3 = threading.Thread(target=receive_msg_thread, args=(c2, NODEC))
    elif addr3[0] == CADDR:
        t3 = threading.Thread(target=receive_msg_thread, args=(c3, NODEC))
    

    # Start threads
    t1.start()
    t2.start()
    t3.start()


    # Get info from user, build message
    flag = True
    while flag:

        # Used to hold the message for the protocol
        messageA = "ALRT" + SERVER + NODEA  # Message from server to node A
        messageB = "ALRT" + SERVER + NODEB  # Message from server to node B
        messageC = "ALRT" + SERVER + NODEC  # Message from server to node C

        # List of all messages. Easier for appending same information
        messages = [messageA, messageB, messageC]

        # Get event type from user
        print("Select an event to run")
        print("Options: Off (0), Fire (1), Tornado (2), Intruder (3), General Emergency (4), Happy Event (5)")
        event = int(input("Input event type: "))
        
        # Cases for events
        if event == 0 or (event < 0 or event > 5):
            messages = add_to_messages(messages, OFF)
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

        # Append direction to messages
        messages[0] += directionA
        messages[1] += directionB
        messages[2] += directionC

        # Append location to all messages
        messages = add_to_messages(messages, location)

        # Time amount to run for
        print("Amount of time to run for")
        print("Input number of 10 second intervals to run for")
        print("Example: 30 is 5 minutes, 01 is 10 seconds")
        print("Max is 5 minutes, 00 is off, 99 is infinite")
        runAmount = input("Run time: ")

        # Append run amount to all messages
        messages = add_to_messages(messages, runAmount)

        # Send correct message to correct node
        # NODE A
        if addr1[0] == AADDR:
            c1.send(str.encode(messages[0]))
        elif addr2[0] == AADDR:
            c2.send(str.encode(messages[0]))
        elif addr3 == AADDR:
            c3.send(str.encode(messages[0]))
            
        # NODE B
        if addr1[0] == BADDR:
            c1.send(str.encode(messages[1]))
        elif addr2[0] == BADDR:
            c2.send(str.encode(messages[1]))
        elif addr3[0] == CADDR:
            c3.send(str.encode(messages[1]))
        
        # NODE C
        if addr1[0] == CADDR:
            c1.send(str.encode(messages[2]))
        elif addr2[0] == CADDR:
            c2.send(str.encode(messages[2]))
        elif addr3[0] == CADDR:
            c3.send(str.encode(messages[2]))
        
    s.close()   # Close server
        
if __name__ == "__main__":
    main()