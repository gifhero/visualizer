from RPi.GPIO import *
import time
import threading

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

def coloff(anode):
    output(anode, LOW)
    output(40, LOW)
    output(38, LOW)
    output(36, LOW)
    output(32, LOW)
    output(22, LOW)
    output(18, LOW)
    output(16, LOW)
    output(14, LOW)


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

levels = []
changed = False

def updateLevels():
    rawCava = raw_input()
    cava = []
    for char in rawCava.split(';'):
        if char >= 48 && char <= 57: 
            i = int(char)
            if value < LEVEL1:
                levels.append(0)
            elif value < LEVEL2:
                levels.append(1)
            elif value < LEVEL3:
                levels.append(2)
            elif value < LEVEL4:
                levels.append(3)
            elif value < LEVEL5:
                levels.append(4)
            elif value < LEVEL6:
                levels.append(5)
            elif value < LEVEL7:
                levels.append(6)
            elif value < LEVEL8:
                levels.append(7)
            else:
                levels.append(8)
    changed = True  

def leds():
    if changed:
        col(7, levels[0])
        time.sleep(0.00001)
        coloff(7)
        col(11, levels[1])
        time.sleep(0.00001)
        coloff(11)
        col(13, levels[2])
        time.sleep(0.00001)
        coloff(13)
        col(15, levels[3])
        time.sleep(0.00001)
        coloff(15)
        col(29, levels[4])
        time.sleep(0.00001)
        coloff(29)
        col(31, levels[5])
        time.sleep(0.00001)
        coloff(31)
        col(33, levels[6])
        time.sleep(0.00001)
        coloff(33)
        col(35, levels[7])
        time.sleep(0.00001)
        coloff(35)
        changed = False


getInputs = threading.Thread(target=updateLevels)
getInputs.setDaemon()
getInputs.start()
while(1):
    leds()

