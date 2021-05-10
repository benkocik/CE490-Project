'''
Programmers: Ben Kocik, Parker Authier, Ava Zaremski
Description: LED test code
'''
# Imports
#import rpi_ws281x
import board
import neopixel
import time
import random


# turn off
def off(num):
    for led in range(num):
        pixels[led] = (0, 0, 0)

def left(num, r, g, b):
    for led in range(num):
        pixels[led] = (r, g, b)
        time.sleep(0.1)

def randomLED(num):
    for led in range(num):
        pixels[random.randint(0, num)] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        time.sleep(0.1)

# Number of LEDs
LED_COUNT = int(input("Number of LEDs on strip: "))
pixels = neopixel.NeoPixel(board.D18, LED_COUNT)

print("Filling LEDs with a cool color")
pixels.fill((200, 40, 200))

print("1:off, 2:left, 3:randomLED")

while test != 0:
    test = int(input("What test would you like to run? "))
    if test == 1:
        off(LED_COUNT)
    if test == 2:
        left(LED_COUNT, 0, 0, 255)
    if test == 3:
        randomLED(LED_COUNT)

# Im sorry parker but the below is getting commented out :(
'''
#Setup 
LED_COUNT = 60
LED_PIN = 18
LED_FREQ_HZ = 8000000
# LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False

#Strip initialization
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

#initialize all LEDs off
off()
        
#direct toward the right
def right(width, time):
    for x in range(0, strip.numPixels(), 1):
        strip.setPixel(x, Color(1,1,1))
        if(x > width):
            strip.setPixel(x-1, Color(0,0,0))

#direct toward the left
def left(width, time):
    for x in range(0, strip.numPixels(), 1):
        strip.setPixel(x, Color(0,0,0))
        if(x > width):
            strip.setPixel(x-1, Color(1,1,1))

#directed toward center
def center(width, time):
    for x in range(0, strip.numPixels(), 1):
        strip.setPixel(x, Color(0,0,0))
        if(x > width):
            strip.setPixel(x-1, Color(1,1,1))

#all off
def off():
    for i in range(0, strip.numPixels(), 1):
        strip.setPixel(i, Color(0,0,0))

#set brightness of strip
def brightness(bright):
    strip.setBrightness(bright)
    return 
'''
