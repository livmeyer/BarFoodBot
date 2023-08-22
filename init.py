from pydub import AudioSegment
from pydub.playback import play
import threading
import os

#Thread For Playing audio
def audio ():
    file = os.getcwd() + '/Audio/Song1.mp3'
    print("Playing audio from: " + file)
    song = AudioSegment.from_mp3(file)
    play(song)


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
