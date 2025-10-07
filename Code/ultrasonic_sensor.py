import RPi.GPIO as GPIO
import time

# Pin setup
TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    # Trigger the sensor
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # 10micro seconds pulse
    GPIO.output(TRIG, False)

    # Wait for ECHO start
    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    # Wait for ECHO end
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    # Calculate distance (Speed of sound = 34300 cm/s)
    elapsed = stop_time - start_time
    distance = (elapsed * 34300) / 2
    return distance

try:
    while True:
        dist = get_distance()
        print(f"Distance: {dist:.2f} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()

