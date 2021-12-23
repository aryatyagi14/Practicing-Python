import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)
GPIO.setup(20, GPIO.OUT)

while True:
    button = GPIO.input(16)
    print(button)
    if( button == 0):
        GPIO.output(20, True)
    else:
        GPIO.output(20, False)
    
