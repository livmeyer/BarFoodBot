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
    set_led_state('idle')
    idle_audio()
    coin_listener()
    stop_audio()

    #Playing Game
    set_led_state('playing')
    play_game_audio()
    result = photo_listener()
    stop_audio()
    if result == 0:
        set_led_state('los')
        play_lose_sound()
    else :
        set_led_state('win')
        play_win_sound()





