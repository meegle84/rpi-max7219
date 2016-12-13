#!/usr/bin/env python
import time
from random import randrange

import max7219.led as led
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

# create matrix device
device = led.matrix(cascaded=1)
print("Created device")

# start demo
device.letter(0, ord('p'))
time.sleep(1)
device.letter(0, ord('u'))
time.sleep(1)
device.invert(1)
device.letter(0, ord('k'))
time.sleep(1)
device.invert(0)
device.letter(0, ord('n'))
time.sleep(1)
device.clear()
