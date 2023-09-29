import RPi.GPIO as GPIO
import time

#set GPIO pins to be connected
#Column pins
C1 = 23
C2 = 24
C3 = 25
C4 = 8

#Row pins
L1 = 7
L2 = 1
L3 = 12
L4 = 16
L5 = 20

#Initialize the GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)
GPIO.setup(L5, GPIO.OUT)

#Configure input pins to use internal pull-down resistors
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# The readLine function implements the procedure discussed in the article
# It sends out a single pulse to one of the rows of the keypad
# and then checks each column for changes
# If it detects a change, the user pressed the button that connects the given line
# to the detected column

def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        print(characters[0])
    if(GPIO.input(C2) == 1):
        print(characters[1])
    if(GPIO.input(C3) == 1):
        print(characters[2])
    if(GPIO.input(C4) == 1):
        print(characters[3])
    GPIO.output(line, GPIO.LOW)

try:
    while True:
        # call the readLine function for each row of the keypad
        readLine(L1, ["F1","F2","#","*"])
        readLine(L2, ["1","2","3","UP"])
        readLine(L3, ["4","5","6","DOWN"])
        readLine(L4, ["7","8","9","ESC"])
        readLine(L5, ["LEFT","0","RIGHT","ENT"])
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("\nApplication stopped!")
