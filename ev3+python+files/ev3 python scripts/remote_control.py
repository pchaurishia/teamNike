#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import InfraredSensor
from time import sleep

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
ir = InfraredSensor()  # Set the remote to channel 1

def top_left_channel_1_action(state):
    if state: # if state == True (pressed)
        steer_pair.on(steering=0, speed=40)
    else:
        steer_pair.off()

def bottom_left_channel_1_action(state):
    if state:
        steer_pair.on(steering=0, speed=-40)
    else:
        steer_pair.off()

def top_right_channel_1_action(state):
    if state:
        steer_pair.on(steering=100, speed=30)
    else:
        steer_pair.off()

def bottom_right_channel_1_action(state):
    if state:
        steer_pair.on(steering=-100, speed=30)
    else:
        steer_pair.off()

# Associate the event handlers with the functions defined above
ir.on_channel1_top_left = top_left_channel_1_action
ir.on_channel1_bottom_left = bottom_left_channel_1_action
ir.on_channel1_top_right = top_right_channel_1_action
ir.on_channel1_bottom_right = bottom_right_channel_1_action

while True:
    ir.process()
    sleep(0.01)
