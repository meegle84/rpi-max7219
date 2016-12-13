#!/usr/bin/env python
import time
from random import randrange, randint

import max7219.led as led
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

# create matrix device
device = led.matrix(cascaded=1)
print("Created device")

time.sleep(1)
for x in range(16):
    for y in range(16):
	device.pixel(randint(0,7),randint(0,7),randint(0,1),True)
        time.sleep(0.1)

device.clear()
