#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from time import sleep

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)

# gentle turn left
steer_pair.on_for_rotations(steering=-25, speed=75, rotations=2); sleep(1)
# same as above but using degrees instead of rotations
steer_pair.on_for_degrees(steering=-25, speed=75, degrees=720); sleep(1)
# turn right on the spot for 3 seconds
steer_pair.on_for_seconds(steering=100, speed=40, seconds=3); sleep(1)
# equivalent to above
steer_pair.on(steering=100, speed=40)
sleep(3)
steer_pair.off()
