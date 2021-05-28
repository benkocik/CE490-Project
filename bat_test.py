# Programmer: Ben Kocik
# Description: Battery test for nodes

import LEDCommands as lc
import random

# Number of LEDs
LEDS = 50

# Init
pixels = lc.init(LEDS)

# Runs forever
while True:
    # Select a random color
    color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    # Run fowards then backwards.
    lc.directForward(pixels, color, 5, 100)
    #lc.directBackward(pixels, color)
