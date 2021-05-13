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
        time.sleep(0.01)

def randomLED(num):
    for led in range(num):
        pixels[random.randint(0, num-1)] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        time.sleep(0.1)

def pulse(length, num, r, g, b, direction="left"):
    off(num)
    if direction == "left":
        led = 0
        while True:
            if led > num:
                led = 0
            for i in range(length):
                pixels[led] = (r, g, b)
                led += 1
            behind = led-length
            if behind < 0:
                behind -= (num + length)
            pixels[behind] = (0, 0, 0)
    # should go the opposite way
    if direction == "right":
        led = num
        while True:
            if led < 0:
                led = num
            for i in range(length):
                pixels[led] = (r, g, b)
                led -= 1
            behind = num - led
            if behind < 0:
                behind -= (num + length)
            pixels[behind] = (0, 0, 0)

def center(num, r, g, b):
    off(num)
    middle = num/2
    start = 0
    end = num

    while True:
        pixels[start] = (r, g, b)
        pixels[end] = (r, g, b)

        start += 1
        end -= 1

        pixels[start -1] = (0, 0, 0)
        pixels[end + 1] = (0, 0, 0)
        
        if(start > middle):
            pixels[middle] = (0, 0, 0)
            start = 0;
        if(end < middle):
            end = num
            

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def rainbow_cycle(num):
    for j in range(255):
        for i in range(num):
            pixel_index = (i * 256 // num) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(0.1)


# Number of LEDs
LED_COUNT = int(input("Number of LEDs on strip: "))
pixels = neopixel.NeoPixel(board.D18, LED_COUNT)

print("Filling LEDs with a cool color")
pixels.fill((255, 255, 255))

print("1:off, 2:left, 3:randomLED, 4:pulse left, 5:pulse right, 6:all on high, 7:all on low, 8:all on medium, 9:rainbow")

test = -1
while test != 0:
    test = int(input("What test would you like to run? "))
    if test == 1:
        off(LED_COUNT)
    if test == 2:
        left(LED_COUNT, 0, 0, 255)
    if test == 3:
        randomLED(LED_COUNT)
    if test == 4:
        pulse(5, LED_COUNT, 60, 5, 120)
    if test == 5:
        pulse(5, LED_COUNT, 5, 120, 170, "right")
    if test == 6:
        pixels.fill((255, 255, 255))
    if test == 7:
        pixels.fill((1, 1, 1))
    if test == 8:
        pixels.fill((120, 120, 120))
    if test == 9:
        rainbow_cycle(LED_COUNT)


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
