#!/usr/bin/env python3
from sys import stderr
from time import sleep
for i in range (8):
    for j in range (7):
        print(i*7+j, end=' ', file=stderr)
    print('', file=stderr)
sleep(8)
