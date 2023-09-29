
from RPLCD import *
from time import sleep
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27)

lcd.cursor_pos = (0, 0)
lcd.write_string('Hello world')
sleep(5)

#next line
lcd.crlf()

#clear screen
lcd.close(clear=True)

#off backlight
lcd.backlight_enabled = False
