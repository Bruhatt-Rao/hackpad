# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here - based on your schematic
# SW1 -> GPIO28 (D2)
# SW2 -> GPIO29 (D3) 
# SW3 -> GPIO6 (D4)
# SW4 -> GPIO7 (D5)
# SW5 -> GPIO0 (D6)
# SW6 -> GPIO1 (D7)
PINS = [
    board.D2,  # SW1 - GPIO28
    board.D3,  # SW2 - GPIO29
    board.D4,  # SW3 - GPIO6
    board.D5,  # SW4 - GPIO7
    board.D6,  # SW5 - GPIO0
    board.D7,  # SW6 - GPIO1
]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  # Switches pull to GND when pressed
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [
        KC.A,                                                           # SW1: Letter A
        KC.DELETE,                                                      # SW2: Delete key
        KC.MACRO("Hello world!"),                                       # SW3: Type "Hello world!"
        KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),         # SW4: Cmd+S (Save)
        KC.Macro(Press(KC.LCMD), Tap(KC.C), Release(KC.LCMD)),         # SW5: Cmd+C (Copy)
        KC.Macro(Press(KC.LCMD), Tap(KC.V), Release(KC.LCMD)),         # SW6: Cmd+V (Paste)
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()