#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)

steer_pair.on_for_degrees(steering=100, speed=20, degrees=930)
