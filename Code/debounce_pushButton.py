from gpiozero import LED,Button
from time import sleep
led = LED(25)
button = Button(2)
previous_state = 1
current_state = 0

while True:
   if button.is_pressed:
      if previous_state != current_state:
         led.on()
         current_state = 1
         print("LED is ON!!")
         sleep(0.15)

      else:
         led.off()
         current_state = 0
         print("LED is Off!!")
         sleep(0.15)
