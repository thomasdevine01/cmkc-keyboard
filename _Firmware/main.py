#==================================
# This code is meant to be a sanity check after assembling the circuits on the PCB.
# and flashing the uC. We can check that every button is "seen" when we press it.
#==================================

print("Hello World!")

import board
import digitalio
import time


from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation



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
# Rotary Encoder push button
#==================================
SW = digitalio.DigitalInOut(board.P0_11)
SW.direction = digitalio.Direction.INPUT
SW.pull = digitalio.Pull.UP

#print(dir(board))  #shows all pins names on uC


#from kb import KMKKeyboard
keyboard = KMKKeyboard()

#keyboard.matrix = "MatrixScanner"
#keyboard.matrix = "MatrixScanner"

print("Starting")



col_pins = [
        board.P1_00,
        board.P0_17,
        board.P0_22,
        board.P0_20,
        #board.P0_31
    ]


row_pins = [
    board.P0_29,
    board.P0_02,
    board.P1_15,
    board.P1_13,
    board.P1_11,
]
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.col_pins = col_pins
keyboard.row_pins = row_pins

keyboard.keymap = [
    # Base Layer
    [
        KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC, KC.NO, KC.NO,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.DELETE, KC.NO,
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.NO, KC.ENTER, KC.HOME, KC.NO,
        KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT, KC.NO, KC.UP, KC.END, KC.NO, 
        KC.LCTRL, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.SPACE, KC.NO, KC.NO, KC.RALT, KC.MO(1), KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.NO, KC.NO,
    ],
    
    # Function Layer
    [
        KC.TILDE, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.TRNS, KC.NO, KC.NO,
        KC.TRNS, KC.BT_PREV_CONN, KC.BT_NEXT_CONN, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.PGUP, KC.NO,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.PGDN, KC.NO, KC.NO,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    ],
]


print("here bottom of main.py")
if __name__ == '__main__':
    keyboard.debug = True
    keyboard.go()