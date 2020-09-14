#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sound import Sound
from sys import stderr
from time import sleep

ts = TouchSensor()
sound = Sound()

ts.wait_for_bump()
sound.beep()

while True:
    print(ts.is_pressed)   # Print to EV3 screen
    print(ts.is_pressed, file=stderr) # Print to VS Code terminal
    sleep(0.5)
