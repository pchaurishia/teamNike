#!/usr/bin/env python3
from ev3dev2.sound import Sound
from time import sleep

sound = Sound()

#play a standard beep
sound.beep()
sleep(2) # pause for 2 seconds

# Play a SINGLE 2000 Hz tone for 1.5 seconds
sound.play_tone(2000, 1.5)
sleep(2)

# Play a SEQUENCE of tones
sound.tone([(200, 2000, 400),(800, 1800, 2000)])
sleep(2)

# Play a 500 Hz tone for 1 second and then wait 0.4 seconds
# before playing the next tone 
# Play the tone three times
# [(500, 1000, 400)] * 3 is the same as
# [(500, 1000, 400), (500, 1000, 400), (500, 1000, 400)]
sound.tone([(500, 1000, 400)] * 3)
sleep(2)

#text to speech
sound.speak('Hello, my name is E V 3!')
