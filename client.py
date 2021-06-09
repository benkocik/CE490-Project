'''
Programmers: Ben Kocik, Parker Authier, Ava Zaremski
Project Description: Code for a device that provides illuminated directional information for building hallways
Code Description: Client code to receive information from server and other clients/nodes.
'''

# Imports
import sys
import socket
from LEDCommands import *      # Commands for LED code

# Main function definition
def main( currNode ):
    # Init LEDs
    LED_COUNT = 50
    pixels = init_led(LED_COUNT)
    color = (0,0,0)

    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Configure port
    PORT = 12345
    HOST = "192.168.1.123"   #TODO Address of the server

    # Waits for server to become available
    connected = False
    while not connected:
        try:
            # Connect to the server
            s.connect((HOST, PORT))
            connected = True
        except Exception:
            pass

    # Data placeholder in case of no data on first loop(s)
    data = "oooooooooooooo"

    flag = True
    while flag:
        # Get data from server
        rawData = s.recv(1024)
        if not rawData:
            pass
        else:
            data = rawData.decode('utf-8')
            print(str(data))    # Print for debugging purposes

        # Parse data for messages
        messageType = data[0:4]
        sender = data[4:6]
        receiver = data[6:8]
        eventType = data[8:10]
        direction = data[10]
        location = data[11:13]

        # Determine what to do based on message
        if messageType == "ALRT":
            # Check correct node
            if receiver == currNode:
                # Off
                if eventType == "00":
                    turnOff(pixels)
                # Fire
                elif eventType == "01":
                    color = (255,0,0)
                    # Flash
                    if direction == "0":
                        fireWarning( pixels )
                    # Left
                    elif direction == "1":
                        for i in range( int(location) ):
                            directForward( pixels, color )
                    # Right
                    elif direction == "2":
                        for i in range( int(location) ):
                            directBackward( pixels, color )
                    # Arrived
                    elif direction == "3":
                        for i in range( int(location) ):
                            arrived( pixels, color )
                # Tornado
                elif eventType == "02":
                    color = (255,255,255)
                    # Flash
                    if direction == "0":
                        tornadoWarning( pixels )
                    # Left
                    elif direction == "1":
                        for i in range( int(location) ):
                            directForward( pixels, color )
                    # Right
                    elif direction == "2":
                        for i in range( int(location) ):
                            directBackward( pixels, color )
                    # Arrived
                    elif direction == "3":
                        for i in range( int(location) ):
                            arrived( pixels, color )
                # Intruder
                elif eventType == "03":
                    color = (0,0,255)
                    # Flash
                    if direction == "0":
                        colorFlash( pixels, color )
                    # Left
                    elif direction == "1":
                        for i in range( int(location) ):
                            directForward( pixels, color )
                    # Right
                    elif direction == "2":
                        for i in range( int(location) ):
                            directBackward( pixels, color )
                    # Arrived
                    elif direction == "3":
                        for i in range( int(location) ):
                            arrived( pixels, color )
                # General Emergency
                elif eventType == "04":
                    color = (255,255,0)
                    # Flash
                    if direction == "0":
                        colorFlash( pixels, color)
                    # Left
                    elif direction == "1":
                        for i in range( int(location) ):
                            directForward( pixels, color )
                    # Right
                    elif direction == "2":
                        for i in range( int(location) ):
                            directBackward( pixels, color )
                    # Arrived
                    elif direction == "3":
                        for i in range( int(location) ):
                            arrived( pixels, color )
                # Happy event
                elif eventType == "99":
                    color = (0,255,0)
                    # Flash
                    if direction == "0":
                        colorFlash( pixels, color )
                    # Left
                    elif direction == "1":
                        for i in range( int(location) ):
                            directForward( pixels, color )
                    # Right
                    elif direction == "2":
                        for i in range( int(location) ):
                            directBackward( pixels, color )
                    # Arrived
                    elif direction == "3":
                        for i in range( int(location) ):
                            arrived( pixels, color )
    
    #TODO Decide on closing
    s.close()
    
if __name__ == "__main__":
    # First argument is receiver, this will be different on each node
    main(sys.argv[0])
