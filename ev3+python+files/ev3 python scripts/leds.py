#!/usr/bin/env python3
from ev3dev2.led import Leds
from time import sleep

leds = Leds()

leds.all_off() # Turn all LEDs off. This also turns off the flashing.
sleep(1)

leds.set_color('LEFT', 'AMBER')
sleep(4)
