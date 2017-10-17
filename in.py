from RPi.GPIO import *
import time
import csv

pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 14, 15, 18, 23, 24, 25, 8, 7]

setmode(BCM)
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
	on(7)
	on(8)
	on(25)
	on(24)
	on(23)
	on(18)
	on(15)
	on(14)
	on(anode)

alloff()
while(1):
    alloff()
    col(9, 8)
    time.sleep(0.001)
    alloff()
    col(10, 8)
    time.sleep(0.001)
     alloff()
    col(22, 8)
    time.sleep(0.001)
    alloff()
    col(27, 8)
    time.sleep(0.001)
    alloff()
    col(17, 8)
    time.sleep(0.001)
    alloff()
    col(4, 8)
    time.sleep(0.001)
    alloff()
    col(3, 8)
    time.sleep(0.001)
    alloff()
    col(2, 8)
    time.sleep(0.001)
