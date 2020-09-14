#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sound import Sound
from time import sleep

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
gyro = GyroSensor()
sound = Sound()

steer_pair.on(steering=0, speed=20)
gyro.wait_until_angle_changed_by(15)
steer_pair.off()
# play_type=1 does NOT block the program while the sound is playing
sound.play_file('/home/robot/sounds/Backing alert.wav',play_type=1)
steer_pair.on_for_rotations(steering=0, speed=-25, rotations=2)
