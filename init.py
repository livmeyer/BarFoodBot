from audio import *
from led import *
from coin import *
from photores import *

import threading
import time
import os


thread_audio = threading.Thread(target=idle_audio, args=())
thread_led = threading.Thread(target=idle_led, args=())
thread_coin = threading.Thread(target=coinListener, args=())
thread_photres = threading.Thread(target=photores_listener, args=())


#Waiting for coin
thread_coin.start()
thread_audio.start()
thread_led.start()
thread_coin.join()
thread_audio.join()
thread_led.join()

#Player Plays Game
thread_photres.start()
thread_photres.join()
