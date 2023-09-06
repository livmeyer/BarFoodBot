import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
pin_number = 17  # Replace with the GPIO pin number you're using
GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

def coin_listener():
    while GPIO.input(pin_number) == 0:
        time.sleep(0.1) 

def photo_listener():
    for i in range(590):
        if GPIO.input(pin_number) == 0:
            return 1  
        time.sleep(0.1)
    return 0

    
