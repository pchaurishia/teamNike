#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep

us = UltrasonicSensor()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)

def limit(value):
    # returns a value within the range -100 to +100
    return min(max(value,-100),+100)

while True:
    error = us.distance_centimeters -15
    # Try changing the proportionality constant in the next line
    steer_pair.on(steering=limit(error*3), speed=30)
    sleep(0.01) # wait for 0.01 seconds
