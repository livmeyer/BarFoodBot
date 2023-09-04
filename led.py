import spidev
import ws2812
import time

spi = spidev.SpiDev()
spi.open(0,0)

phase = 0
state = 'idle'
rate = 1

idle_lights = [[[0,0,0]] * 100] * 7
win_lights = [[[0,0,0]] * 100] * 7
los_lights = [[[0,0,0]] * 100] * 7
game_lights = [[[0,0,0]] * 100] * 7

current_lights = [[0,0,0]] * 100

def blink():
    phase = 0 
    while True:
        if state == 'idle':
                current_lights = idle_lights [phase]
        elif state ==  'win':
                phase = win_lights [phase]
        elif state ==  'los':
                phase = win_lights [phase]
        elif state == 'playing':   
                phase = win_lights [phase]
        phase = (phase + 1) % 7
        ws2812.write2812(spi, current_lights)
        time.sleep(rate)

def set_led_rate (new_rate):
    rate = new_rate

def set_led_state (new_state):
    print('State Changed from: ' + state + ', to: ' + new_state)
    state = new_state

