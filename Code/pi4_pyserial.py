import serial
import time

ser = serial.Serial('/dev/ttyUSB0',
                    baudrate=115200,
		    parity=serial.PARITY_NONE,
		    stopbits=serial.STOPBITS_ONE)

while True:
    b = ser.readline().decode().strip()
    print(b)

pmd.reset_output_buffer()
