from audio import *
from led import *
from coin import *

import threading
import time
import os

led_Thread = threading.Thread(target=blink, args=())
led_Thread.start()

while True:
    #Waiting for Coin
    print("Waiting for Coin")
    set_led_state('idle')
    idle_audio()
    time.sleep(2)
    coin_listener()
    #stop_audio()

    #Playing Game
    play_game_audio()
    print("Game Started")
    set_led_state('playing')
    
    time.sleep(2)
    result = photo_listener()
    stop_audio()
    reset_phase()
    if result == 0:
        print("You lost")
        set_led_state('los')
        play_lose_sound()
    else :
        print ("You Won")
        set_led_state('win')
        play_win_sound()
    time.sleep(5)
    stop_audio()




