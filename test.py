import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
pin_number = 17
GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while GPIO.input(pin_number) != GPIO.LOW:
        time.sleep(0.1)
    print("Coin Inserted")

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
