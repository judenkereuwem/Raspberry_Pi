import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1015()

GAIN = 1

while True:
    value = adc.read_adc(0, gain=GAIN)
    print(value)
    time.sleep(0.5)
