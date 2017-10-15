from RPi.GPIO import *
import time
import csv

pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 14, 15, 18, 23, 24, 25, 8, 7]

setmode(BCM)
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

def alloff(pin):
	for pin in pins:
		output(pin, LOW)

while(1):
	# gets cava output and appends to list
    rawCava = input()
    cava = []
    colVals = []
    for char in rawCava.split(';'):
            cava.append(char)
    # removes whitespace added at end
    cava = cava[:-1]
    # converts each row value to the appropriate level
    for value in cava:
    	if value < LEVEL1:
    		rowVals.append(0)
    	elif value < LEVEL2:
    		rowVals.append(1)
    	elif value < LEVEL3:
    		rowVals.append(2)
     	elif value < LEVEL4:
    		rowVals.append(3)
    	elif value < LEVEL5:
    		rowVals.append(4)
    	elif value < LEVEL6:
    		rowVals.append(5)
    	elif value < LEVEL7:
    		rowVals.append(6)
    	elif value < LEVEL8:
    		rowVals.append(7)
    	else:
    		rowVals.append(8)
    alloff()
    col1(rowVals[0])
#    col2(rowVals[1])
#    col3(rowVals[2])
#    col4(rowVals[3])
#    col5(rowVals[4])
#    col6(rowVals[5])
#    col7(rowVals[6])
#    col8(rowVals[7])

def col1(level):
	print(level)
	on(10)
	if level < 8:
		on(7)
	if level < 7:
		on(8)
	if level < 6:
		on(25)
	if level < 5:
		on(24)
	if level < 4:
		on(23)
	if level < 3:
		on(18)
	if level < 2:
		on(15)
	if level < 1:
		on(14)
