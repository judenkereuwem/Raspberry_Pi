import RPi.GPIO as GPIO
import time

# Set GPIO mode and pin numbers
GPIO.setmode(GPIO.BCM)

# Define RGB LED pin numbers
red_pin = 6   # Replace with the GPIO pin number connected to the red LED
green_pin = 13  # Replace with the GPIO pin number connected to the green LED
blue_pin = 19   # Replace with the GPIO pin number connected to the blue LED

# Setup GPIO pins
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

# Function to set RGB color
def set_rgb_color(red, green, blue):
    GPIO.output(red_pin, red)
    GPIO.output(green_pin, green)
    GPIO.output(blue_pin, blue)

# Function to turn off RGB LED
def turn_off():
    set_rgb_color(0, 0, 0)

# Example: Blink through different colors
try:
    while True:
        set_rgb_color(1, 0, 0)  # Red
        time.sleep(1)
        set_rgb_color(0, 1, 0)  # Green
        time.sleep(1)
        set_rgb_color(0, 0, 1)  # Blue
        time.sleep(1)
except KeyboardInterrupt:
    turn_off()
    GPIO.cleanup()
