from RPi.GPIO import *
import time
import csv

pins = [7,11,12,13,15,18,16,22,29,31,32,33,35,36,37,38,40]

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
	if level < 8:
		on(40)
	if level < 7:
		on(38)
	if level < 6:
		on(36)
	if level < 5:
		on(32)
	if level < 4:
		on(22)
	if level < 3:
		on(18)
	if level < 2:
		on(16)
	if level < 1:
		on(12)
	on(anode)

alloff()
while(1):
	# gets cava output and appends to list
    rawCava = raw_input()
    cava = []
    colVals = []
    for char in rawCava.split(';'):
            cava.append(char)
    # removes whitespace added at end
    cava = cava[:-1]
    # converts each row value to the appropriate level
    for value in cava:
    	value = int(value)
    	if value < LEVEL1:
    		colVals.append(0)
    	elif value < LEVEL2:
    		colVals.append(1)
    	elif value < LEVEL3:
    		colVals.append(2)
     	elif value < LEVEL4:
    		colVals.append(3)
    	elif value < LEVEL5:
    		colVals.append(4)
    	elif value < LEVEL6:
    		colVals.append(5)
    	elif value < LEVEL7:
    		colVals.append(6)
    	elif value < LEVEL8:
    		colVals.append(7)
    	else:
    		colVals.append(8)
    alloff()
    col(7, colVals[0])
    time.sleep(0.00001)
    alloff()
    col(11, colVals[1])
    time.sleep(0.00001)
    alloff()
    col(13, colVals[2])
    time.sleep(0.00001)
    alloff()
    col(15, colVals[3])
    time.sleep(0.00001)
    alloff()
    col(29, colVals[4])
    time.sleep(0.00001)
    alloff()
    col(31, colVals[5])
    time.sleep(0.00001)
    alloff()
    col(33, colVals[6])
    time.sleep(0.00001)
    alloff()
    col(35, colVals[7])
    time.sleep(0.00001)
