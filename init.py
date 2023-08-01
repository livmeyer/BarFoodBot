#from playsound import playsound
import threading 

def audio ():
    print("Playing audio")

def led ():
    print("Leds Activated")

# Create two threads
threadAudio = threading.Thread(target=audio, args=())
threadLED = threading.Thread(target=led, args=())


threadAudio.start()
threadLED.start()

threadAudio.join()
threadLED.join()

print("All threads have finished.")