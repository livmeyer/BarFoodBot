import pygame
import os
import threading
import time


def queue_daemon():
    global current_song
    while True:
        time.sleep(60)  
        if idle_chanel.get_queue() == None:
            print('Adding to queue')
            idle_chanel.queue(songs[current_song])
            current_song = (current_song + 1) % song_count
           

def idle_audio ():
    game_chanel.pause()
    idle_chanel.unpause()

def play_game_audio ():
    idle_chanel.pause()
    game_chanel.unpause()
    game_chanel.play(game_music, loops = -1)

def play_win_sound ():
    game_chanel.play(win)

def play_lose_sound ():
    game_chanel.play(loose)


pygame.init()
pygame.mixer.init()
idle_chanel = pygame.mixer.Channel(0)
idle_chanel.set_volume(0.75)
game_chanel = pygame.mixer.Channel(1)

file = os.getcwd() + '/Audio/'
game_music = pygame.mixer.Sound(file + 'game.wav')
loose = pygame.mixer.Sound(file + 'loose.wav')
win = pygame.mixer.Sound(file + 'win.wav')
songs = []

song_count = 2
current_song = 1


for i in range(song_count):
    songs.append(pygame.mixer.Sound(file + 'Songs/lsong'+ str(i + 1) + '.wav'))

idle_chanel.play(songs[0])

queue_Thread = threading.Thread(target=queue_daemon, args=())
queue_Thread.start()