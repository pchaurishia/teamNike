#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

cl = ColorSensor()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)

while True:
    steer_pair.on(steering=(cl.ambient_light_intensity * 2)-100, speed=30)
    sleep(0.1) # wait for 0.1 seconds
