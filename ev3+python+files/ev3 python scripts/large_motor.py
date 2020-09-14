#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B
from ev3dev2.motor import SpeedDPS, SpeedRPS, SpeedRPM
from time import sleep

large_motor = LargeMotor(OUTPUT_B)

# We'll make the motor turn 180 degrees
# at speed 50 (525 dps for the large motor)
large_motor.on_for_degrees(speed=50, degrees=180)
# then wait one second
sleep(1)
# then – 180 degrees at 500 dps
large_motor.on_for_degrees(speed=SpeedDPS(500), degrees=-180)
sleep(1)
# then 0.5 rotations at speed 50 (525 dps)
large_motor.on_for_rotations (speed=50, rotations=0.5)
sleep(1)
# then – 0.5  rotations at 1 rotation per second (360 dps)
large_motor.on_for_rotations (speed=SpeedRPS(1), rotations=-0.5)
