
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

RelayPin = 26

GPIO.setup(RelayPin, GPIO.OUT)

while True:
    GPIO.output(RelayPin, GPIO.LOW)
    sleep(2)
    GPIO.output(RelayPin, GPIO.HIGH)
    sleep(2)
