#==================================
# This code is meant to be a sanity check after assembling the circuits on the PCB.
# and flashing the uC. We can check that every button is "seen" when we press it.
#==================================

print("Hello World!")

import board
import digitalio
import time


from digitalio import DigitalInOut, Direction, Pull




#==================================
# E and LE pins
#==================================
    #LE needs to be high
    #E needs to be low
LE = digitalio.DigitalInOut(board.P0_24)
LE.direction = digitalio.Direction.OUTPUT
LE.value = 1

E = digitalio.DigitalInOut(board.P0_31)
E.direction = digitalio.Direction.OUTPUT
E.value = 0

#==================================
# CLD pins
#==================================
CLD1 = digitalio.DigitalInOut(board.P1_00)
CLD1.direction = digitalio.Direction.OUTPUT
CLD1.value = 0

CLD2 = digitalio.DigitalInOut(board.P0_17)
CLD2.direction = digitalio.Direction.OUTPUT
CLD2.value = 0

CLD3 = digitalio.DigitalInOut(board.P0_22)
CLD3.direction = digitalio.Direction.OUTPUT
CLD3.value = 0

CLD4 = digitalio.DigitalInOut(board.P0_20)
CLD4.direction = digitalio.Direction.OUTPUT
CLD4.value = 0

#==================================
# ROW pins
#==================================
ROW1 = digitalio.DigitalInOut(board.P0_29)
ROW1.direction = digitalio.Direction.INPUT
ROW1.pull = Pull.DOWN

ROW2 = digitalio.DigitalInOut(board.P0_02)
ROW2.direction = digitalio.Direction.INPUT
ROW2.pull = Pull.DOWN

ROW3 = digitalio.DigitalInOut(board.P1_15)
ROW3.direction = digitalio.Direction.INPUT
ROW3.pull = Pull.DOWN

ROW4 = digitalio.DigitalInOut(board.P1_13)
ROW4.direction = digitalio.Direction.INPUT
ROW4.pull = Pull.DOWN

ROW5 = digitalio.DigitalInOut(board.P1_11)
ROW5.direction = digitalio.Direction.INPUT
ROW5.pull = Pull.DOWN


print(dir(board))  #shows all pins names on uC


cols = [CLD1, CLD2, CLD3, CLD4]
rows = [ROW1, ROW2, ROW3, ROW4, ROW5]


#reset columns
for i in range(3):
    cols[i].value = 0
    print("i is", i)
    




while True:

# this looks stupid, but we need to toggle every "bit" in our "cols" variable so that we can count from 0-14 in binary.
# State machine looks like: select column, check all rows, tell us which button is pressed based on col,row 
    for d in range(2): #bit 3
        cols[3].value = d
        for c in range(2): #bit 2
            cols[2].value = c
            for b in range(2): #bit 1
                cols[1].value = b
                for a in range(2): #bit 0
                    cols[0].value = a
                    for j in range(5):
                        if rows[j].value:
                            col = ((8*d) + (4*c) + (2*b )+ a)
                            print("Button column: ", col, ", row: ", j, " pressed")
                            time.sleep(0.1)
