import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
pin_number = 17  # Replace with the GPIO pin number you're using
GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def coin_listener():
    print("Listing for Coins")
    while GPIO.LOW != GPIO.input(pin_number):            
        time.sleep(0.1)
    print("Coin Inserted")    
    

