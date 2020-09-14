#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sound import Sound
from time import sleep

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
ts = TouchSensor()
sound = Sound()

while True: # forever
    steer_pair.on(steering=0, speed=30)
    ts.wait_for_pressed()
    # play_type=1 means 'Play the sound without blocking the program'
    sound.play_file('/home/robot/sounds/Backing alert.wav',play_type=1)
    # Back up along a curved path
    steer_pair.on_for_rotations(steering=-20, speed=-25, rotations=3)
