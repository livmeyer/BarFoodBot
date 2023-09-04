import pygame
import os
import threading
import time

SONG_COUNT = 1
CURRENT_SONG = 1



def idle_audio ():
    Song.play()

def stop_audio ():
    pygame.mixer.stop()

def play_game_audio ():
    print("Stop Idle Audio")

def play_moan ():
    print("Moaning Audio")

def play_lose_sound ():
    print("Losing Audio")


pygame.init()
pygame.mixer.init()

file = os.getcwd() + '/Audio/Song1.wav'
Song = pygame.mixer.Sound(file)