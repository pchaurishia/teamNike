#!/usr/bin/env python3
# Ensure (using the separate script) that the pen is raised before launching this script
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C, MediumMotor
from time import sleep
from math import sqrt, pi, atan2, degrees
from ev3dev2.sound import Sound
from time import sleep
medium_motor = MediumMotor()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
sound = Sound()
my_string = 'ALIKE'.upper()# Use only characters AEFHIKLMN. upper() converts lowercase to upper
wf = 1 # wheel factor. Use 1 for home version and 0.77 for edu version.
scl = 3 # Scale. scl=3 gives 3cm per grid unit. Use scl values between 3 and 5.
sp = 20 # speed of steer_pair. Use values between 15 and 30.
sep = 10.5 # effective wheel separation in centimeters.
degs_per_cm = 26.84 * wf # degrees of wheel turn per cm advanced.
degs_per_robot_deg = 2.46 * wf # angle wheels turn when robot turns one degree on the spot
medium_motor.position = 0 # needed to protect against a bug.
# 'direction' is the direction from the current node to the next node, measured cw from 'north'.
heading = 90 # 'heading' is the direction the robot is facing, measured clockwise from 'north'. 

sequence={'A':'GiMbo','E':'GhCamo','F':'GhCam','H':'aGiCo','I':'AcBnMo'}
sequence.update({'K':'aCgo','L':'Amo','M':'ahco','N':'aoc'})

node={'a':(0,4),'b':(1,4),'c':(2,4),'d':(0,3),'e':(1,3),'f':(2,3),'g':(0,2)}
node.update({'h':(1,2),'i':(2,2),'j':(0,1),'k':(1,1)})
node.update({'l':(2,1),'m':(0,0),'n':(1,0),'o':(2,0),'q':(2.6,0)}) # Note the value of 'q'

def pu():
    if abs(medium_motor.position) > 10: # if pen is not already up
        medium_motor.on_to_position(speed=50, position=0)

def pd():
    if abs(medium_motor.position-180) > 10: # if pen is not already down
        medium_motor.on_to_position(speed=50, position=180)

def get_dist_and_dir(letter):
    dx = node[letter][0] - current_node[0]
    dy = node[letter][1] - current_node[1]
    distance = sqrt(dx**2+dy**2) # Pythagoras!
    angle = atan2(dy,dx)  # 'Cartesian' angle in radians ccw from east
    # convert to angle in degrees cw from north, in range 0-360
    direction = (90-degrees(angle))%360 
    return distance, direction # as a TUPLE

def move_straight(letter):
    global current_node, heading
    if letter.islower():  # lower the pen if necessary
        pd()
    else:   # raise the pen if necessary
        pu()
    letter = letter.lower() # set the letter to lower case
    distance, direction = get_dist_and_dir(letter)
    turn_angle = direction - heading
    turn_angle = ((turn_angle+180)%360)-180  # get turn angle into range -180° to 180°
    turn(turn_angle) # make the turn!
    advance(distance)  # make the robot advance!
    heading = heading + turn_angle  # modify heading since the robot has just turned
    current_node = [node[letter][0], node[letter][1]] # update current_node

def turn(turn_angle):
    steer_pair.on_for_degrees(steering=100,speed=sp,degrees=turn_angle*degs_per_robot_deg)
def advance(distance):
    degs = distance*scl*degs_per_cm
    steer_pair.on_for_degrees(steering=0,speed=sp,degrees=degs)

for char in my_string:
    sound.speak(char)
    # set current_node to equal [0,0] (node M) each time we start writing a character
    current_node=[0,0]  
    for letter in (sequence[char]+'Q'): # add Q to put space between the characters
        move_straight(letter)
