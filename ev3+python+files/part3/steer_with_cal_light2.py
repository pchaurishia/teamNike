#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from time import sleep

cl = ColorSensor()
btn = Button()
sound = Sound()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)

def limit(value):  # returns a value within the range -100 to +100
    return min(max(value,-100),+100)

sound.speak('Press any key when the sensor is in dim light')
btn.wait_for_bump('enter')
dim = cl.ambient_light_intensity
sound.beep()

sound.speak('Press any key when the sensor is in bright light')
btn.wait_for_bump('enter')
bright = cl.ambient_light_intensity
sound.beep()
sound.speak('3, 2, 1, go!')

while not btn.any(): # Press any key to exit
    #intensity = min(max(cl.ambient_light_intensity,dim),bright)
    intensity = cl.ambient_light_intensity
    steer = limit((200*(intensity-dim)/(bright-dim))-100)
    # steer = (200*(intensity-dim)/(bright-dim))-100
    # steer = min(max(steer,-100),+100)
    steer_pair.on(steering=steer, speed=30)
    sleep(0.1) # wait for 0.1 seconds
