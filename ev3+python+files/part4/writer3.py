#!/usr/bin/env python3
# Copyright Nigel Ward, May 2019.   See http://ev3python.com
# If necessary, use the separate script to make sure that the
# pen is raised before running this script
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C, MediumMotor
from sys import stderr
from math import sqrt, pi, atan2, degrees
from ev3dev2.sound import Sound
from time import sleep

medium_motor = MediumMotor()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
sound = Sound()

my_string = 'BLACK'.upper()  # Use only characters ABCDEFGHIJKLMN and 0123456789.
wf = 1 # wheel factor. Use 1 for home version and 0.77 for edu version.
scl = 3 # Scale. Use scl values between 3 and 6.
sp = 20 # speed of steer_pair. Use values between 15 and 25.
sep = 10.5 # effective wheel separation in centimeters.
degs_per_cm = 26.84 * wf # degrees of wheel turn per cm advanced.
degs_per_robot_deg = 2.46 * wf # angle wheel turns through when robot turns one degree.
medium_motor.position = 0 # needed to protect against a bug.
# 'direction' is the direction from the current node to the next node, measured cw from 'north'.
heading = 90 # 'heading' is the direction the robot is facing, measured clockwise from 'north'.
go_forwards = True # initially the robot will move forwards (for positive distance values).

sequence={'A':'GiMbo','B':'abVgHYm','C':'Ftjx','D':'abUlYm','E':'GhCamo','F':'GhCam'}
sequence.update({'G':'FtjxKlo','H':'aGiCo','I':'AcBnMo','J':'AclW','K':'aCgo'})
sequence.update({'L':'Amo','M':'ahco','N':'aoc'})
sequence.update({'0':'JdUlW','1':'DbnMo','2':'DUmo','3':'DVW'})
sequence.update({'4':'Ljco','5':'nvgac','6':'JXWdU','7':'ca','8':'NvSVy','9':'Jxftu'})

node={'a':(0,4),'b':(1,4),'c':(2,4),'d':(0,3),'e':(1,3),'f':(2,3),'g':(0,2)}
node.update({'h':(1,2),'i':(2,2),'j':(0,1),'k':(1,1)})
node.update({'l':(2,1),'m':(0,0),'n':(1,0),'o':(2,0),'q':(2.6,0)})
node.update({'s':(1,4),'t':(0,3),'u':(2,3),'v':(1,2),'w':(0,1),'x':(2,1),'y':(1,0)})

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
    direction = (90-degrees(angle))%360 # convert to degrees cw from north, in range 0-360
    print('distance to node:'+str(distance)+'  direction to node:'+str(direction),file=stderr)
    return distance, direction # as a TUPLE

def move_straight(letter, current_node, heading):
    print('node letter:'+letter+'  robot heading:'+str(int(heading)),file=stderr)
    if letter.islower():  # lower the pen if necessary
        pd()
    else:   # raise the pen if necessary
        pu()
    letter = letter.lower() # set the letter to lower case
    distance, direction = get_dist_and_dir(letter)
    turn_angle = direction - heading
    turn_angle = ((turn_angle+180)%360)-180  # get turn angle into range -180° to 180°
    if abs(turn_angle)>90:
        turn_angle = ((turn_angle+270)%360)-90 # get into range -90° to 90°
        go_forwards = False
    else:
        go_forwards = True
    print('turn_angle:'+str(turn_angle)+'  go_forwards:True', file=stderr)
    print('medium_motor.position (0=up, 180=down): '+str(int(medium_motor.position))+'\n',file=stderr)
    turn(turn_angle) # make the turn!
    advance(distance, go_forwards)  # make the robot advance!
    heading = heading + turn_angle  # modify heading since the robot has just turned
    current_node = [node[letter][0], node[letter][1]] # update current_node
    return current_node, heading

def draw_arc(letter, current_node, heading): # so that we can avoid using the global keyword
    pd() # make sure the pen is down
    print('node letter:'+letter+'  robot heading:'+str(int(heading)),file=stderr)
    cw = letter.isupper() # uppercase means draw arc clockwise (cw)
    letter = letter.lower() # set the letter to lower case
    distance, direction = get_dist_and_dir(letter)
    if distance==2: # semicircle
        arc_angle = 180
        if cw:
            hs = direction-90        # hs = heading at start of arc
            he = (direction+90)%360  # he = heading at end of arc
        else:
            hs = direction+90
            he = (direction-90)%360
    else: # quarter circle
        arc_angle = 90
        if cw: # if arc is to be drawn clockwise
            hs = direction-45        # hs =  heading for start of arc
            he = (direction+45)%360  # he =  heading at end of arc
        else:
            hs = direction+45
            he = (direction-45)%360
    turn_angle = hs - heading
    turn_angle = ((turn_angle+180)%360)-180  # get turn angle into range -180° to 180°
    turn(turn_angle) # make the turn!
    steering = (-1+2*cw)*100*sep/(2*scl+sep) # from drawbot code
    degs = arc_angle*(2*scl+sep)*wf/4.32
    print('arc_angle:'+str(arc_angle), end='', file=stderr)
    print('  steering:'+ str(int(steering))+'  degs:'+str(int(degs))+'\n', file=stderr) 
    steer_pair.on_for_degrees(steering, sp, degs)
    heading = he    # update the heading value now that the robot has moved
    current_node = [node[letter][0], node[letter][1]]
    return current_node, heading # so that we can avoid using the global keyword
    
def turn(turn_angle):
    steer_pair.on_for_degrees(steering=100,speed=sp,degrees=turn_angle*degs_per_robot_deg)

def advance(distance, go_forwards):
    degrees = (-1+2*go_forwards)*distance*scl*degs_per_cm
    steer_pair.on_for_degrees(steering=0,speed=sp,degrees=degrees)

for char in my_string:
    sound.speak(char)
    print('Letter to write: '+char+'\n', file=stderr)
    # set current_node to equal [0,0] each time we start writing a character
    current_node=[0,0]  
    for letter in (sequence[char]+'Q'): # add Q to put space between the characters
        arc_nodes = 'STUVWXY'
        if letter.upper() not in arc_nodes:
            current_node, heading = move_straight(letter, current_node, heading)
        else:
            current_node, heading = draw_arc(letter, current_node, heading)
