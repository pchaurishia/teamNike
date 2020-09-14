#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import GyroSensor
from sys import stderr
from time import sleep

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
gyro = GyroSensor()

steer_pair.on_for_seconds(steering=100, speed=20, seconds=6, block=False)

for i in range(15):
    print('Angle and Rate: ' + str(gyro.angle_and_rate), file=stderr)
    sleep(0.5)
