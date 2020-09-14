#!/usr/bin/env python3
from ev3dev2.sound import Sound
from time import sleep

sound = Sound()

sound.play_file('/home/robot/sounds/MINDSTORMS.wav')
sound.beep()
