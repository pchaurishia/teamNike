#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import InfraredSensor
from time import sleep

ir = InfraredSensor()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)

def limit(value):
    # returns a value within the range -100 to +100
    return min(max(value,-100),+100)

while True:
    # for a light-colored wall, multiply
    # proximity by 0.7 to obtain APPROXIMATE distance in cm
    distance = ir.proximity * 0.7
    error = distance - 15
    # Try changing the proportionality constant in the next line
    steer_pair.on(steering=limit(error*3), speed=30)
    sleep(0.01) # wait for 0.01 seconds
