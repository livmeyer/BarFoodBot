import spidev
import ws2812
import time

def blink():
    global state
    global rate
    global phase
    phase = 0
    while True:
        if state == 'idle':
                current_lights = idle_lights [phase]
        elif state ==  'win':
                current_lights = win_lights [phase]
        elif state ==  'los':
                current_lights = los_lights [phase]
        elif state == 'playing':   
                current_lights = game_lights [phase]
        phase = (phase + 1) % 7
        ws2812.write2812(spi, current_lights)
        time.sleep(rate)

def set_led_rate (new_rate):
    global rate
    rate = new_rate

def set_led_state (new_state):
    global state
    state = new_state

def reset_phase ():
      global phase
      phase = 0

spi = spidev.SpiDev()
spi.open(0,0)

state = 'idle'
rate = 2
phase = 0

idle_lights = [[[100,0,0]] * 100, [[0,0,0]] * 100, [[100,0,0]] * 100, [[0,0,0]] * 100,  [[100,0,0]] * 100, [[0,0,0]] * 100,  [[100,0,0]] * 100 ]
win_lights = [[[0,100,0]] * 100] * 7
los_lights = [[[100,0,0]] * 100] * 7
game_lights = [[[75,75,0]] * 100] * 7

current_lights = [[0,0,0]] * 100
