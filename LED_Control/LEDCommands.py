#import rpi_ws281x
import board
import neopixel
import time

# Define functions which animate LEDs in various ways.
#color is a 3-length array with values for red,green,and blue

def turnOff( pixels ):
    pixels.fill(0,0,0)


def solidColor(pixels, color):
    "Displays a solid color"
    pixels.fill(color[0], color[1], color[2])

def colorFlash(pixels, color, wait_ms = 50):
    "Flashes a solid color once"
    solidColor(pixels,color)
    time.sleep(wait_ms / 1000.0)
    
    turnOff(pixels)
    time.sleep(wait_ms / 1000.0)

def fireWarning(pixels):
    "Performs specific pattern to indicate fire emergency"
    fire = (255,0,0)

    solidColor(pixels,fire)
    time.sleep(100 / 1000.0)

    turnOff(pixels)
    time.sleep(50 / 1000.0)

    solidColor(pixels,fire)
    time.sleep(50 / 1000.0)

    turnOff(pixels)
    time.sleep(50 / 1000.0)

    solidColor(pixels,fire)
    time.sleep(100 / 1000.0)



def tornadoWarning(pixels):
    "Performs specific pattern to indicate tornado emergency"
    tornado = (127,127,127)

    for i in range(5):
        solidColor(pixels,tornado)
        time.sleep(100 / 1000.0)
    
        turnOff(pixels)
        time.sleep(50 / 1000.0)



def directForward(pixels, color, wait_ms = 50):
    "Wipe color across display a pixel at a time."
    for i in range(pixels.len):
        pixels[i] = (color[0],color[1],color[2])
        pixels.show()
        time.sleep(wait_ms / 1000.0)
        turnOff(pixels)

def directBackward(strip, color, wait_ms = 50):
    "Wipe color across display a pixel at a time."
    for i in range(pixels.len):
        pixels[pixels.len - i] = (color[0],color[1],color[2])
        pixels.show()
        time.sleep(wait_ms / 1000.0)
        turnOff(pixels)

def arrived(pixels, color, wait_ms = 50):
    "Color flashes outward into center to display arrival"
    center = pixels.len / 2
    for i in range(center):
        pixels[i] = (color[0],color[1],color[2])
        pixels[pixels.len - i] = (color[0],color[1],color[2])
        pixels.show()
        time.sleep(wait_ms / 1000.0)
        turnOff(pixels)


# Number of LEDs
LED_COUNT = int(input("Number of LEDs on strip: "))
pixels = neopixel.NeoPixel(board.D18, LED_COUNT)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

print("Filling LEDs with a cool color")
pixels.fill((255, 255, 255))

print("1:off, 2:Solid Color, 3:Solid Color Flash, 4:Direct Forward, 5:Direct Backward, 6:Arrived, 7:Tornado, 8:Fire")

test = -1
while test != 0:
    test = int(input("What test would you like to run? "))
    if test == 1:
        turnOff(pixels)
    if test == 2:
        solidColor(pixels, red)
        solidColor(pixels,green)
        solidColor(pixels,blue)
    if test == 3:
        colorFlash(pixels, red)
        colorFlash(pixels,green)
        colorFlash(pixels,blue)
    if test == 4:
        directForward(pixels,red)
        directForward(pixels,green)
        directForward(pixels,blue)
    if test == 5:
        directBackward(pixels,red)
        directBackward(pixels,green)
        directBackward(pixels,blue)
    if test == 6:
        arrived(pixels,red)
        arrived(pixels,green)
        arrived(pixels,blue)
    if test == 7:
        tornadoWarning(pixels)
    if test == 8:
        fireWarning(pixels)