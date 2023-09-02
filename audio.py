import pygame
import os

SONG_COUNT = 1
CURRENT_SONG = 1



#Thread For Playing audio
def idle_audio ():
    file = os.getcwd() + '/Audio/Song1.mp3'
    pygame.mixer.music.load(file)
    print("Playing audio form :" + file)
    pygame.mixer.music.play()
    
    print("Song finished")

pygame.init()
pygame.mixer.init()
idle_audio()