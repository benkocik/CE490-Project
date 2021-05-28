import neopixel
import time
import board

# Define functions which animate LEDs in various ways.
#color is a 3-length array with values for red,green,and blue

def turnOff( pixels ):
    pixels.fill((0,0,0))
    pixels.show( )


def solidColor(pixels, color):
    "Displays a solid color"
    pixels.fill((color[0], color[1], color[2]))
    pixels.show()

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



def directForward(pixels, color, length=3, wait_ms = 50):
    "Wipe color across display a pixel at a time."
    pixels[len(pixels)-1] = (0, 0, 0)
    for i in range(len(pixels)):
        for n in range(length):
            if i+n < len(pixels):
                pixels[i+n] = (color[0],color[1],color[2])
        if i-1 >= 0:
            pixels[i-1] = (0, 0, 0)
        #pixels.show()
        time.sleep(wait_ms / 1000.0)
        

def directBackward(pixels, color, wait_ms = 50):
    "Wipe color across display a pixel at a time."
    for i in range(len(pixels)):
        pixels[len(pixels) - i] = (color[0],color[1],color[2])
        pixels.show()
        time.sleep(wait_ms / 1000.0)
        turnOff(pixels)

def arrived(pixels, color, wait_ms = 50):
    "Color flashes outward into center to display arrival"
    center = len(pixels) / 2
    for i in range(center):
        pixels[i] = (color[0],color[1],color[2])
        pixels[len(pixels) - i] = (color[0],color[1],color[2])
        pixels.show()
        time.sleep(wait_ms / 1000.0)
        turnOff(pixels)

def init(LED_COUNT):
    pixels = neopixel.NeoPixel(board.D18, LED_COUNT)
    return pixels

# Main function for testing.
def main():
    # Number of LEDs
    LED_COUNT = int(input("Number of LEDs on strip: "))
    pixels = neopixel.NeoPixel(board.D18, LED_COUNT)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)

    print("Filling LEDs with a cool color")
    pixels.fill((0, 255, 255))
    pixels.show()

    print("1:off, 2:Solid Color, 3:Solid Color Flash, 4:Direct Forward, 5:Direct Backward, 6:Arrived, 7:Tornado, 8:Fire")

    test = -1
    while test != 0:
        test = int(input("What test would you like to run? "))
        if test == 1:
            turnOff(pixels)
            time.sleep(10)
        if test == 2:
            solidColor(pixels, red)
            time.sleep(10)
            solidColor(pixels,green)
            time.sleep(10)
            solidColor(pixels,blue)
            time.sleep(10)
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

if __name__ == "__main__":
    main()