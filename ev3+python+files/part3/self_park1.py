#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)

wf = 1  # Set wf to 1 for home version and 0.77 for edu version
# Adjust steer and rots until the robot moves neatly out of the traffic lane
steer = 28
rots = -1.8
steer_pair.on_for_rotations(steering=0, speed=25, rotations=3.7*wf)
steer_pair.on_for_rotations(steering=steer, speed=15, rotations=rots*wf)
steer_pair.on_for_rotations(steering=-steer, speed=15, rotations=rots*wf)
steer_pair.on_for_rotations(steering=0, speed=25, rotations=0.7*wf)
