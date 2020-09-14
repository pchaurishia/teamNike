#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep

us = UltrasonicSensor()
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)

while True:
    distance = us.distance_centimeters
    if  distance > 15:
        # medium turn right
        tank_pair.on(left_speed=30, right_speed=25)
    elif distance > 13:
        # go straight
        tank_pair.on(left_speed=30, right_speed=30)
    else:
        # medium turn left
        tank_pair.on(left_speed=25, right_speed=30)
    sleep(0.01) # wait for 0.01 seconds
