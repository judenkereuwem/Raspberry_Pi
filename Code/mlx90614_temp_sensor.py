from smbus2 import SMBus
from mlx90614 import MLX90614
import time

bus = SMBus(1)

sensor = MLX90614(bus, address=0x5A)
while True:
    print("Ambient temp: ", sensor.get_ambient())
    print("Object temp: ", sensor.get_object_1())
    print(" ")
    time.sleep(0.5)
    #bus.close()
