import pygame
import os
import threading
import time

SONG_COUNT = 7
CURRENT_SONG = 1
ONIDLE = False


def idle_audio ():
    global CURRENT_SONG, SONG_COUNT
    CURRENT_SONG = (CURRENT_SONG + 1) % SONG_COUNT

def stop_audio ():
    pygame.mixer.stop()

def play_game_audio ():
    game_music.play()

def play_win_sound ():
    win.play()

def play_lose_sound ():
    loose.play()


pygame.init()
pygame.mixer.init()

file = os.getcwd() + '/Audio/'
game_music = pygame.mixer.Sound(file + 'game.wav')
loose = pygame.mixer.Sound(file + 'loose.wav')
win = pygame.mixer.Sound(file + 'win.wav')
songs = []

for i in range(SONG_COUNT):
    songs.append(pygame.mixer.Sound(file + 'Songs/song'+ str(i + 1) + '.wav'))