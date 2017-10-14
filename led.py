#from RPi.GPIO import *
import time
import csv

# defines what cava values equal which leds
LEVEL1 = 5
LEVEL2 = 12
LEVEL3 = 18
LEVEL4 = 24
LEVEL5 = 32
LEVEL6 = 39
LEVEL7 = 45
LEVEL8 = 50


# gets cava output and appends to list
highest = 0
i = 0
while(1):
    rawCava = input()
    cava = []
    for char in rawCava.split(';'):
            cava.append(char)
    cava = cava[:-1]
    for value in cava:


asdfasdf
