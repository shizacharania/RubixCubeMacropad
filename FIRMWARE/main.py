'''
SwiftPad
'''
import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display.ssd1306 import SSD1306

# Pinout
COL0 = board.D3
COL1 = board.D4
COL2 = board.D5
ROW1 = board.D0
ROW2 = board.D1
ROW3 = board.D2

keyboard = KMKKeyboard()

#matrix settings
keyboard.col_pins = (COL0, COL1, COL2)
keyboard.row_pins = (ROW0, ROW1, ROW2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Keymap
keyboard.keymap = [
    [KC.LCTRL(KC.TAB)]

if __name__ == '__main__':
    keyboard.go()