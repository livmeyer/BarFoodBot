from audio import *
from led import *
from coin import *
#from photores import *

import threading
import time
import os



while True:
    idle_audio()
    coin_listener()
    stop_audio()


