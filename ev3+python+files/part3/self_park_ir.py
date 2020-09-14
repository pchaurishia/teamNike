#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MoveSteering, OUTPUT_B, OUTPUT_C, SpeedDPS
from ev3dev2.sensor.lego import InfraredSensor
from sys import stderr
from time import sleep

motorB = LargeMotor(OUTPUT_B)
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
ir = InfraredSensor()

wf = 1
motorB.position = 0
steer_pair.on(steering=0, speed=SpeedDPS(265))
while motorB.position*0.377 < 370:
    if ir.proximity * 0.7 < 16.5:
        motorB.position = 0
    print(motorB.position*0.377, ir.proximity * 0.7, file = stderr)
    sleep(0.1)

steer = 28
rots = -1.8
steer_pair.on_for_rotations(steering=0, speed=25, rotations=0.5*wf)
steer_pair.on_for_rotations(steering=steer, speed=15, rotations=rots*wf)
steer_pair.on_for_rotations(steering=-steer, speed=15, rotations=rots*wf)
steer_pair.on_for_rotations(steering=0, speed=25, rotations=0.7*wf)


