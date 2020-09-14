#!/usr/bin/env python3
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sound import Sound
from time import sleep

us = UltrasonicSensor()
sound = Sound()

while True:
    if us.distance_centimeters < 255:
        sound.beep()
    sleep (0.5)
