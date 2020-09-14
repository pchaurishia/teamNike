#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import InfraredSensor
from time import sleep

ir = InfraredSensor()
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)

while True:
    # for a light-colored wall, multiply
    # proximity by 0.7 to obtain APPROXIMATE distance in cm
    distance = ir.proximity * 0.7
    if  distance > 6:
        # medium turn right
        tank_pair.on(left_speed=40, right_speed=35)
    elif distance < 4:
        # medium turn left
        tank_pair.on(left_speed=35, right_speed=40)
    else:
        # go straight
        tank_pair.on(left_speed=40, right_speed=40)

    sleep(0.01) # wait for 0.01 seconds
