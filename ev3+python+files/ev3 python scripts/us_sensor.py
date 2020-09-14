#!/usr/bin/env python3
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.led import Leds
from sys import stderr
from time import sleep

us = UltrasonicSensor()
leds = Leds()

leds.all_off() # Needed, to stop the LEDs flashing
while True:
    if us.distance_centimeters < 40: # to detect objects closer than 40cm
        # In the above line you can also use inches: us.distance_inches < 16
        leds.set_color('LEFT',  'RED')
        leds.set_color('RIGHT', 'RED')
    else:
        leds.set_color('LEFT',  'GREEN')
        leds.set_color('RIGHT', 'GREEN')
    print(us.distance_centimeters, file=stderr)
    sleep (0.5)
