from pydub import AudioSegment
from pydub.playback import play

import os

SONG_COUNT = 1
CURRENT_SONG = 1


#Thread For Playing audio
def idle_audio ():
    print("Playing audio form :" + file)
    play(song)
    print("Song finished")


file = os.getcwd() + '/Audio/Song1.mp3'
song = AudioSegment.from_mp3(file)