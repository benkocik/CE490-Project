
import rpi_ws281x


#Setup 
LED_COUNT = 0
LED_PIN = 0
LED_FREQ_HZ = 8000000
LED_DMA = 10
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


