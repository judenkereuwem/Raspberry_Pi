
import RPi.GPIO as GPIO
import time

sensor = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)

while True:
        if GPIO.input(sensor):
		print("Object detected")
		while GPIO.input(sensor):
			time.sleep(0.2)
	else:
		print("No detection")
