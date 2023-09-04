import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
pin_number = 17  # Replace with the GPIO pin number you're using
GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def coin_listener():
    while GPIO.LOW != GPIO.input(pin_number):            
        time.sleep(0.1)  

def photo_listener():
    for i in range(590):
        if GPIO.LOW == GPIO.input(pin_number):
            return 1  
        time.sleep(0.1)
    return 0

    
