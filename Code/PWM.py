	
from gpiozero import PWMLED
from time import sleep

led1 = PWMLED(20)


try:
  while True:
    #fade in
    for duty_cycle in range(0, 100, 1):
      led1.value = duty_cycle/100.0
      sleep(0.02)

    #fade out
    for duty_cycle in range(100, 0, -1):
      led1.value = duty_cycle/100.0
      sleep(0.02)
      
except KeyboardInterrupt:
  print("Stop the program and turning off the LED")
  led1.value = 0
  pass
