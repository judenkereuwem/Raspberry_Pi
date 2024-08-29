
from gpiozero import Button
from time import sleep

button = Button(21)

while True:
        print(button.is_pressed)
	sleep(0.01)
