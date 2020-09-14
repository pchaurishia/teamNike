#!/usr/bin/env python3
# Before running the drawbot script, run this script and
# use the left and right buttons
# to make the medium motor cam point upwards.

from ev3dev2.motor import MediumMotor
from ev3dev2.button import Button
from time import sleep

medium_motor = MediumMotor()
btn = Button()

# Press left button to turn medium motor left (counterclockwise)
def left(state):
    if state: # if state = True
        medium_motor.on(speed=-10)
    else:
        medium_motor.stop()

# Press right button to turn medium motor right (clockwise)
def right(state):
    if state:
        medium_motor.on(speed=10)
    else:
        medium_motor.stop()

btn.on_left = left
btn.on_right = right

while True:  # This loop checks buttons state continuously, 
             # calls appropriate event handlers
    btn.process() # Check for currently pressed buttons.
    # If the new state differs from the old state,
    # call the appropriate button event handlers.
    sleep(0.01)  # buttons state will be checked every 0.01 second
