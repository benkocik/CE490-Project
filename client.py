'''
Programmers: Ben Kocik, Parker Authier, Ava Zaremski
Project Description: Code for a device that provides illuminated directional information for building hallways
Code Description: Client code to receive information from server.
'''

# Imports
import sys
import time
import socket
from LEDCommands import *      # Commands for LED code
import RPi.GPIO as GPIO

# Main function definition
def main( currNode ):
    # Init LEDs
    LED_COUNT = 50
    pixels = init_led(LED_COUNT)
    color = (0,0,0)

    sendTime = time.time()

    # Initialize GPIO for battery check
    batt = "1"                      # 0 == Battery, 1 == Wall
    battPercent = 100               # Holds battery percentage
    expectBatTime = 20              # Amount of time in hours battery can run for
    batTime = expectBatTime * 3600  # Amount of time in seconds battery can run for (used to calc unix epoch)
    batFlag = True                  # Flag for if battery has been turned on or not
    startBat = 0.0
    channel = 16
    GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
            print("Connected to " + HOST + " on port " + str(PORT))
        except Exception:
            pass

    # Data placeholder in case of no data on first loop(s)
    data = "oooooooooooooo"

    flag = True
    while flag:
        # Get data from server
        try:
            rawData = s.recv(1024, socket.MSG_DONTWAIT)
        except BlockingIOError:
            pass
        try:
            data = rawData.decode('utf-8')
            print(str(data))    # Print for debugging purposes
        except NameError:
            pass

        # Parse data for messages
        messageType = data[0:4]
        sender = data[4:6]
        receiver = data[6:8]
        eventType = data[8:10]
        direction = data[10]
        location = data[11:13]
        runAmount = data[13:15]
        
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
                        directForward( pixels, color )
                    # Right
                    elif direction == "2":
                        directBackward( pixels, color )
                    # Arrived
                    elif direction == "3":
                        arrived( pixels, color )
                # Tornado
                elif eventType == "02":
                    color = (255,255,255)
                    # Flash
                    if direction == "0":
                        tornadoWarning( pixels )
                    # Left
                    elif direction == "1":
                        directForward( pixels, color )
                    # Right
                    elif direction == "2":
                        directBackward( pixels, color )
                    # Arrived
                    elif direction == "3":
                        arrived( pixels, color )
                # Intruder
                elif eventType == "03":
                    color = (0,0,255)
                    # Flash
                    if direction == "0":
                        colorFlash( pixels, color )
                    # Left
                    elif direction == "1":
                        directForward( pixels, color )
                    # Right
                    elif direction == "2":
                        directBackward( pixels, color )
                    # Arrived
                    elif direction == "3":
                        arrived( pixels, color )
                # General Emergency
                elif eventType == "04":
                    color = (255,255,0)
                    # Flash
                    if direction == "0":
                        colorFlash( pixels, color)
                    # Left
                    elif direction == "1":
                        directForward( pixels, color )
                    # Right
                    elif direction == "2":
                        directBackward( pixels, color )
                    # Arrived
                    elif direction == "3":
                        arrived( pixels, color )
                # Happy event
                elif eventType == "99":
                    color = (0,255,0)
                    # Flash
                    if direction == "0":
                        colorFlash( pixels, color )
                    # Left
                    elif direction == "1":
                        directForward( pixels, color )
                    # Right
                    elif direction == "2":
                        directBackward( pixels, color )
                    # Arrived
                    elif direction == "3":
                        arrived( pixels, color )
        # Check power status
        if GPIO.input(channel) == 1:
            batt = "1"  # Wall power
            batFlag = True
            battPercent = ""
        elif GPIO.input(channel) == 0:
            batt = "0"  # Battery
            # On first run
            if batFlag:
                startBat = time.time()
                batFlag = False
            # Calculate battery percentage
            battPercent = str(int(round(100-(((time.time() - startBat)/batTime)*100))))
            if len(battPercent) == 2:
                battPercent = "0" + battPercent # Add 0 in front

        # Add error message, can be anything you want up to 50 chars
        errorMsg = ""

        sendMessage = "RECV" + currNode + "00" + batt + battPercent + errorMsg

        # Send status every 5 minutes
        if int(time.time()-sendTime) >= 300:
            s.send(str.encode(sendMessage))
            sendTime = time.time()

    s.close()
    
if __name__ == "__main__":
    # First argument is receiver, this will be different on each node
    main(sys.argv[1])
