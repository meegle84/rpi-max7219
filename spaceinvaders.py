#!/usr/bin/env python
import time
from random import randrange, randint

import max7219.led as led

# create matrix device
device = led.matrix(cascaded=1)
print("Created device")

# start demo
SI_FONT = [
    [0x18, 0x5C, 0xB6, 0x1F, 0x1F, 0xB6, 0x5C, 0x18],
    [0x98, 0x5C, 0xB6, 0x5F, 0x5F, 0xB6, 0x5C, 0x98],
    [0x78, 0x3C, 0xF7, 0x3C, 0x3C, 0xF7, 0x3C, 0x78],
    [0x1e, 0xbc, 0x77, 0x3c, 0x3c, 0x77, 0xbc, 0x1e]
]  # end of CP437_FONT
for i in range(16):
    device.letter(0, i%4, font=SI_FONT)
    time.sleep(0.1)
    device.letter(0, (i+1)%4, font=SI_FONT)
    time.sleep(0.1)

device.clear()
