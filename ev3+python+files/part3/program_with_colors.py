#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from ev3dev2.sound import Sound
from time import sleep

cl = ColorSensor()
ts = TouchSensor()
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
sound = Sound()

def get_color():
    while True:   # Wait for a valid color to be detected
        color = cl.color_name
        if color in ('Blue', 'Green', 'Yellow', 'Red', 'White'):
            sound.speak(color)
            return color
            break   # exit the loop
        sleep(0.1)

color_list = []  # create empty list
while True:
    sound.beep()
    ts.wait_for_bump()
    my_color = get_color() # get a valid color
    if my_color == 'White':
        break  # break out of loop
    else:
        color_list.append(my_color)

sound.play_file('/home/robot/sounds/Horn 2.wav')
for col in color_list:
    if col=='Blue':    # turn the robot 90 degrees left
        # Try degrees=171 for edu version, 222 for home version
        tank_pair.on_for_degrees(-50, 50, degrees=171) # adjust the degrees if necessary
    elif col=='Yellow':# turn the robot 90 degrees right
        tank_pair.on_for_degrees(50, -50, degrees=171) # adjust the degrees if necessary
    elif col=='Green': # go straight forward 2 wheel rotations
        tank_pair.on_for_rotations(50, 50, rotations=2)
    elif col=='Red':   # go straight backwards 2 wheel rotations
        tank_pair.on_for_rotations(-50, -50, rotations=2)
