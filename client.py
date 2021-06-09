'''
Programmers: Ben Kocik, Parker Authier, Ava Zaremski
Project Description: Code for a device that provides illuminated directional information for building hallways
Code Description: Client code to receive information from server and other clients/nodes.
'''

# Imports
import socket
import LEDCommands      # Commands for LED code
import board
import neopixel

# Main function definition
def main( currNode ):
    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Configure port
    PORT = 12345
    HOST = "192.168.1.123"   #TODO figure out address of server

    # Connect to the server on computer
    s.connect((HOST, PORT))

    # Get data from server
    data = s.recv(1024)
    print(str(data))

    LED_COUNT = 50
    pixels = neopixel.NeoPixel(board.D18, LED_COUNT)

    color = (0,0,0)

    messageType = data[0:4]
    sender = data[4:6]
    receiver = data[6:8]
    eventType = data[8:10]
    direction = data[10]
    location = data[11:13]

    if messageType == "ALRT":
        if receiver == currNode:
            if eventType == "00":
                turnOff(pixels)
            elif eventType == "01":
                color = (255,0,0)
                if direction == "0":
                    fireWarning( pixels )
                elif direction == "1":
                    for i in range( int(location) ):
                        directForward( pixels, color )
                elif direction == "2":
                    for i in range( int(location) ):
                        directBackward( pixels, color )
                elif direction == "3":
                    for i in range( int(location) ):
                        arrived( pixels, color )
            elif eventType == "02":
                color = (255,255,255)
                if direction == "0":
                    tornadoWarning( pixels )
                elif direction == "1":
                    for i in range( int(location) ):
                        directForward( pixels, color )
                elif direction == "2":
                    for i in range( int(location) ):
                        directBackward( pixels, color )
                elif direction == "3":
                    for i in range( int(location) ):
                        arrived( pixels, color )
            elif eventType == "03":
                color = (0,0,255)
                if direction == "0":
                    colorFlash( pixels, color )
                elif direction == "1":
                    for i in range( int(location) ):
                        directForward( pixels, color )
                elif direction == "2":
                    for i in range( int(location) ):
                        directBackward( pixels, color )
                elif direction == "3":
                    for i in range( int(location) ):
                        arrived( pixels, color )
            elif eventType == "04":
                color = (255,255,0)
                if direction == "0":
                    colorFlash( pixels, color)
                elif direction == "1":
                    for i in range( int(location) ):
                        directForward( pixels, color )
                elif direction == "2":
                    for i in range( int(location) ):
                        directBackward( pixels, color )
                elif direction == "3":
                    for i in range( int(location) ):
                        arrived( pixels, color )
            elif eventType == "99":
                color = (0,255,0)
                if direction == "0":
                    colorFlash( pixels, color )
                elif direction == "1":
                    for i in range( int(location) ):
                        directForward( pixels, color )
                elif direction == "2":
                    for i in range( int(location) ):
                        directBackward( pixels, color )
                elif direction == "3":
                    for i in range( int(location) ):
                        arrived( pixels, color )

                
                



    #TODO: Decide on closing
    s.close
    

if __name__ == "__main__":
    main( )
