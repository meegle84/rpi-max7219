#!/usr/bin/env python
import time
from random import randrange, randint

import max7219.led as led
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

# create matrix device
device = led.matrix(cascaded=1)
print("Created device")

# start demo
time.sleep(1)
for x in range(8):
    for y in range(8):
        device.pixel(x,y,True,True)
        time.sleep(0.1)
        device.clear()

for x in range(8):
    for y in range(8):
        device.pixel(y,x,True,True)
        time.sleep(0.1)
        device.clear()
device.clear()
