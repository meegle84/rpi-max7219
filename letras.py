#!/usr/bin/env python

import time
from random import randrange

import max7219.led as led
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

# create matrix device
device = led.matrix(cascaded=1)
print("Created device")

# start demo
time.sleep(1)
for x in range(256):
    # device.letter(1, 32 + (x % 64))
    print("letter: ",x)
    device.letter(0, x)
    time.sleep(0.5)
