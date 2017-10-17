from RPi.GPIO import *
import time
import csv

pins = [7,11,12,13,15,18,16,22,29,31,32,33,35,36,37,38,40]

setmode(BOARD)
setwarnings(False)

# setup all the pins and set to LOW
for pin in pins:
	setup(pin, OUT)
	output(pin, LOW)

# defines what cava values equal which leds
LEVEL1 = 5
LEVEL2 = 12
LEVEL3 = 18
LEVEL4 = 24
LEVEL5 = 32
LEVEL6 = 39
LEVEL7 = 45
LEVEL8 = 50

def on(pin):
	output(pin, HIGH)

def off(pin):
	output(pin, LOW)

def alloff():
	for pin in pins:
		output(pin, LOW)

def col(anode, level):
	on(anode)

alloff()
while(1):
    alloff()
    col(7, 8)
    time.sleep(0.00001)
    alloff()
    col(11, 8)
    time.sleep(0.00001)
    alloff()
    col(13, 8)
    time.sleep(0.00001)
    alloff()
    col(15, 8)
    time.sleep(0.00001)
    alloff()
    col(29, 8)
    time.sleep(0.00001)
    alloff()
    col(31, 8)
    time.sleep(0.00001)
    alloff()
    col(33, 8)
    time.sleep(0.00001)
    alloff()
    col(35, 8)
    time.sleep(0.00001)
