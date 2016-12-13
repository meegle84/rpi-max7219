#!/usr/bin/env python

import time
from random import randrange

import max7219.led as led
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

# create matrix device
device = led.matrix(cascaded=1)
print("Created device")

# start demo
msg0 = "ola k ase?"
msg1 = "pa k kieres saber eso jaja saludos"
print(msg0)
device.show_message(msg0, font=proportional(CP437_FONT))
time.sleep(1)

print(msg1)
device.show_message(msg1, font=proportional(CP437_FONT))
time.sleep(1)
