#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
us = UltrasonicSensor()

while True:    # forever
    distance = us.distance_centimeters
    error = distance - 10
    if distance < 50:
        steer_pair.on(steering=0, speed=error*2)
    else:
        steer_pair.off()
    sleep(0.2)
