#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.sensor.lego import GyroSensor
from time import sleep

gyro = GyroSensor()
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)

# Start the left motor with speed 30% to initiate a medium turn right.
tank_pair.on(left_speed=30, right_speed=0)

# Wait until the gyro sensor detects that the robot has turned
# (at least) 45 deg in either direction
gyro.wait_until_angle_changed_by(45)

# Robot moves straight ahead with speed 50% until the wheels
# have turned through two rotations
tank_pair.on_for_rotations(left_speed=50, right_speed=50, rotations=2)
