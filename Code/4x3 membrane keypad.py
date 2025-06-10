#!/usr/bin/env python3

from gpiozero import DigitalOutputDevice, Button
from time import sleep

# Configure rows, columns, and keypad layout
rows_pins = [25, 7, 1, 12]
cols_pins = [16, 20, 21]
keys = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9",
        "*", "0", "#"]

# Initialize row pins as DigitalOutputDevice
rows = [DigitalOutputDevice(pin) for pin in rows_pins]
# Initialize column pins as Buttons
cols = [Button(pin, pull_up=False) for pin in cols_pins]

def read_keypad():
    """
    Read the currently pressed keys on the keypad.
    :return: A list of pressed keys.
    """
    pressed_keys = []
    # Scan each row and column to identify pressed keys
    for i, row in enumerate(rows):
        row.on()  # Enable the current row
        for j, col in enumerate(cols):
            if col.is_pressed:  # Check if the column button is pressed
                # Calculate the key index based on row and column
                index = i * len(cols) + j
                pressed_keys.append(keys[index])
        row.off()  # Disable the current row
    return pressed_keys

# Main loop to continuously read the keypad and print newly pressed keys
last_key_pressed = []

print("Press keys on the keypad. Press Ctrl+C to exit.")
while True:
    pressed_keys = read_keypad()
    if pressed_keys and pressed_keys != last_key_pressed:
        print(*pressed_keys)  # Print the list of pressed keys
        last_key_pressed = pressed_keys
    sleep(0.1)  # Short delay to reduce CPU load
