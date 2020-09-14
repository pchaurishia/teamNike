#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from time import sleep

tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)

# gentle turn left
tank_pair.on_for_rotations(left_speed=50, right_speed=75, rotations=3); sleep(1)
# same as above but using degrees instead of rotations
tank_pair.on_for_degrees(left_speed=50, right_speed=75, degrees=1080); sleep(1)
# turn right on the spot
tank_pair.on_for_rotations(left_speed=-50, right_speed=50, rotations=4); sleep(1)
# go straight forwards for four seconds
tank_pair.on_for_seconds(left_speed=40, right_speed=40, seconds=4); sleep(1)
# equivalent to above
tank_pair.on(left_speed=40, right_speed=40)
sleep(4)
tank_pair.off()
