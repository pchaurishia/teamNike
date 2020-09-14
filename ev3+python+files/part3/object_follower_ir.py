#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import InfraredSensor
from time import sleep

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
ir = InfraredSensor()

while True:    # forever
    # for a largish light-colored object,
    # multiply proximity by 0.7 to obtain distance in cm
    distance = ir.proximity * 0.7
    error = distance - 10
    if distance < 50:
        steer_pair.on(steering=0, speed=error*2)
    else:
        steer_pair.off()
    sleep(0.2)
