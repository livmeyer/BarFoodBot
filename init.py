from playsound import playsound
import threading 

#Thread For Playing audio
def audio ():
    print("Playing audio")
    playsound('./Audio/Song1.mp3')

#Thread Handles Leds
def led ():
    print("Leds Activated")


threadAudio = threading.Thread(target=audio, args=())
threadLED = threading.Thread(target=led, args=())

threadAudio.start()
threadLED.start()

threadAudio.join()
threadLED.join()

print("All threads have finished.")