#!/usr/bin/env python3
# Use the separate script to ensure the cam is pointing up before running this script
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C, MediumMotor
from math import copysign, atan, degrees, sqrt

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
medium_motor = MediumMotor()

shape = 'A' # shape must be one of: pentagram, spiral, squiral, vertex, smiley, A
sp = 25 # speed, try other values if you like
wf = 1  # wheel factor. Use 1 for home version and 0.77 for edu version
degs_per_cm = 26.84 * wf # degrees of wheel turn per cm advanced
degs_per_robot_deg = 2.46 * wf # angle wheel must turn through
# such that the robot turns one degree
def fd(distance):
    steer_pair.on_for_degrees(steering=0, speed=sp, degrees= distance*degs_per_cm)
def bk(distance):
    steer_pair.on_for_degrees(steering=0, speed=sp, degrees=-distance*degs_per_cm)
def lt(angle):
    steer_pair.on_for_degrees(steering=-100, speed=sp, degrees=angle*degs_per_robot_deg)
def rt(angle):
    steer_pair.on_for_degrees(steering= 100, speed=sp, degrees=angle*degs_per_robot_deg)
def arc(angle, r):   # r = radius. Negative radius means draw the arc counterclockwise
    steer_pair.on_for_degrees(copysign(100/(0.19*abs(r) + 1),r), sp, angle*42.16*wf*(abs(r)+5.25)/90)
def pu():
    if abs(medium_motor.position) > 10: # if pen is not already up
        medium_motor.on_to_position(speed=50, position=0)
def pd():
    if abs(medium_motor.position-180) > 10: # if pen is not already down
        medium_motor.on_to_position(speed=50, position=180)

if shape == 'pentagram':
    pd()
    for i in range(5):
        if i%2:
            bk(30)
        else:
            fd(30)
        lt(36)
    pu()

elif shape == 'spiral':
    pd()
    for i in range(1,15,2): # i will start at 1, increase in steps of 2 and finish with 13
        arc(180,i)
    pu()

elif shape == 'vertex':
    pd()
    for i in range(2,32,2): # i will start at 2 and finish at 30 but won't include 32
        fd(i)
        rt(93)
    pu()

elif shape == 'smiley':
    lt(30)
    fd(5)
    pd()
    arc(360,-1.5)
    pu()
    bk(5)
    rt(60)
    fd(5)
    pd()
    arc(360,1.5)
    pu()
    bk(5)
    rt(30)
    bk(5)
    rt(90)
    pd()
    arc(120,-5)
    pu()
    rt(90)
    fd(5)
    rt(90)
    pd()
    arc(360,10)
    pu()

elif shape == 'A':
    scl = 4 # scale. How many cm for each unit of the 4x2 grid
    rt(degrees(atan(0.25)))
    pd()
    fd(scl*sqrt(17))
    lt(2*degrees(atan(0.25)))
    bk(scl*sqrt(17))
    pu()
    rt(degrees(atan(0.25)))
    fd(scl*2)
    lt(90)
    pd()
    fd(scl*2)
    pu()
