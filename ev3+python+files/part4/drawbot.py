#!/usr/bin/env python3
# Use the separate script to ensure the cam is pointing up before running this script
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C, MediumMotor
from math import copysign

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
medium_motor = MediumMotor()

sp = 25 # speed, try other values if you like
wf = 1 # wheel factor. Use 1 for home version and 0.77 for edu version
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
def arc(angle, r):   # r = radius
    #steer_pair.on_for_degrees(100/(0.19*r + 1), sp, angle*42.16*wf*(r+5.25)/90)
    st = copysign(100/(0.19*abs(r) + 1),r)
    steer_pair.on_for_degrees(steering = st, speed = sp, angle*42.16*wf*(abs(r)+5.25)/90)
def pu():
    medium_motor.on_for_degrees(speed=sp, degrees=180)
def pd():
    medium_motor.on_for_degrees(speed=sp, degrees=180)

rt(30)
pd()
fd(15)
lt(60)
bk(15)
lt(60)
fd(15)
pu()
bk(20)
pd()
arc(360, 6) # radius of about 6 is not ideal because it causes slower wheel to move TOO
# slowly and therefore it completes its motion slightly after the faster wheel
pu()


'''
rt(30)
pd()
for i in range(3):
    fd(15)
    if i !=2:
        rt(120)
pu()
bk(20)
pd()
arc(360, 6) # radius of about 6 is not ideal because it causes slower wheel to move TOO
# slowly and therefore it completes its motion slightly after the faster wheel
pu()
'''