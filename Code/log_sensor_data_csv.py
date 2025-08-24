
import os
import pandas as pd
import csv
from datetime import datetime
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time


# Initialize the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)
 
# Create an ADS1115 object
ads = ADS.ADS1115(i2c)
 
# Define the analog input channels
channel0 = AnalogIn(ads, ADS.P0)
channel1 = AnalogIn(ads, ADS.P1)
channel2 = AnalogIn(ads, ADS.P2)
channel3 = AnalogIn(ads, ADS.P3)

# #Get current date and time for naming csv file
now = datetime.now()
d = datetime(1, 1, 1).now()
dtString = d.strftime('{}_{}_{}'.format(d.hour%12,d.minute,d.second))
dString = now.strftime('%d_%m_%Y')


#Create new .csv file
pathDir = 'data'
filename = f'{dString}_{dtString}.csv'
df = pd.DataFrame() 
df.to_csv(f"{pathDir}/{filename}", index=False, encoding='utf-8')

while True:

	#Open csv file and add headers
	with open(f"{pathDir}/{filename}",'r+') as f:
		f.writelines('Time,data')#file header
		
		while True:
			data = channel1.value
			print(data)
	
			#Log incoming data from pico and current time to csv file
			now = datetime.now()
			d = datetime(1, 1, 1).now()
			am_pm = 'am' if d.hour<12 else 'pm'
			dtString = d.strftime('{}:{}:{}:{}'.format(d.hour%12,d.minute,d.second, am_pm))
		
			# #Log incoming data and current time to csv file
			f.writelines(f'\n{dtString},{data}')
			f.flush()
			time.sleep(1)
	


















