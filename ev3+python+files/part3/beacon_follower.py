#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import InfraredSensor
from time import sleep

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
ir = InfraredSensor()

while True:    # forever
    distance = ir.distance()
    if distance:  # If distance is not None
        error = distance - 10
        steer_pair.on(steering=2*ir.heading(), speed=min(90, 3*error))
    else:
        steer_pair.off()
    sleep(0.1)
