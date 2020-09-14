#!/usr/bin/env python3
from ev3dev2.display import Display
from ev3dev2.sound import Sound
from time import sleep

lcd = Display()
sound = Sound()

def show_for(seconds):
    lcd.update()
    sound.beep()
    sleep(seconds)
    lcd.clear()

# Try each of these different sets:
style = 'helvB'
#style = 'courB'
#style = 'lutBS'

y_value = 0
str1 = ' The quick brown fox jumped'
str2 = '123456789012345678901234567890'
for height in [10, 14, 18, 24]:
    text = style+str(height)+str1
    lcd.text_pixels(text, False, 0, y_value, font=style+str(height))
    y_value += height+1   # short for  y_value = y_value+height+1
    lcd.text_pixels(str2, False, 0, y_value, font=style+str(height))
    y_value += height+1
show_for(6)

strings = [] # create an empty list
# Screen width can accommodate 12 fixed
# width characters with widths 14 or 15
#               123456789012
strings.append(style+'24 The')
strings.append('quick brown ')
strings.append('fox jumps   ')
strings.append('over the dog')
strings.append('123456789012')

for i in range(len(strings)):
    lcd.text_pixels(strings[i], False, 0, 25*i, font=style+'24')
show_for(6)
