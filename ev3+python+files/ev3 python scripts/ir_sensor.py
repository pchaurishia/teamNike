#!/usr/bin/env python3
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.led import Leds
from sys import stderr
from time import sleep

ir = InfraredSensor()
leds = Leds()

leds.all_off() # Needed, to stop the LEDs flashing
while True:
    if ir.proximity < 40*1.4: # To convert cm to proximity, multiply by 1.4
        leds.set_color('LEFT',  'RED')
        leds.set_color('RIGHT', 'RED')
    else:
        leds.set_color('LEFT',  'GREEN')
        leds.set_color('RIGHT', 'GREEN')
    print(str(int(ir.proximity*0.7)) + ' cm approx', file=stderr)
    # To convert proximity to cm, multiply by 0.7.
    sleep (0.5)
