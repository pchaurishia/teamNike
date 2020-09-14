#!/usr/bin/env python3
from ev3dev2.display import Display
from textwrap import wrap
from time import sleep

lcd = Display()

def show_text(string, font_name='courB24', font_width=15, font_height=24):
    lcd.clear()
    strings = wrap(string, width=int(180/font_width))
    for i in range(len(strings)):
        x_val = 89-font_width/2*len(strings[i])
        y_val = 63-(font_height+1)*(len(strings)/2-i)
        lcd.text_pixels(strings[i], False, x_val, y_val, font=font_name)
    lcd.update()
    sleep(5)
my_text = 'The quick brown fox jumps over the lazy dog'
show_text(my_text, 'courB14', 9, 14)
show_text(my_text, 'lutBS14', 9, 14)
show_text(my_text, 'courB18', 11, 18)
show_text(my_text, 'lutBS18', 11, 18)
show_text(my_text, 'courB24', 15, 24)
# or simply show_text(my_text) since default values
# have been set for courB24
show_text(my_text, 'lutBS24', 14, 24)
