import serial
import time 
import string
import pynmea2  

while True:

    ser=serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)
    dataout =pynmea2.NMEAStreamReader() 
    newdata=ser.readline()
    #print(newdata)
    #time.sleep(0.5)
    if '$GNRMC' in str(newdata):
        try:
            print(newdata.decode('utf-8', errors='ignore'))
            newmsg=pynmea2.parse(newdata.decode('utf-8'))
            lat=newmsg.latitude 
            lng=newmsg.longitude 
            print(f"Latitude: {lat} and Longitude: {lng}")

        except pynmea2.ParseError:
            print("Could not parse the GPS data")
        except UnicodeDecodeError:
            print("Decoding error occurred, possible invalid bytes")
