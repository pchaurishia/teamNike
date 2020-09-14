#!/usr/bin/env python3
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sound import Sound
from time import sleep

cl = ColorSensor()
sound = Sound()

while True:
    freq = 110*2**(cl.ambient_light_intensity/12)
    sound.play_tone(frequency=freq, duration=0.5)
    sleep(0.1)
