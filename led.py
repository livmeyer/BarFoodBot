import spidev
import ws2812
import time
import os
import csv

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

def read_blink_patern(file_name):
        result = []
        for i in range(amount_phases):
                phase = []
                with open( os.getcwd() + '/LED_Patterns/' + file_name + '/phase' + str(i + 1) + '.csv', mode='r') as csv_file:
                        # Create a CSV reader object
                        csv_reader = csv.reader(csv_file)
    
                        # Loop through each row in the CSV file
                        for row in csv_reader:
                                # Convert each item in the row to an integer and append it to the list
                                int_row = [row]
                                phase.append(int_row)
                result.append(phase)
        return result


spi = spidev.SpiDev()
spi.open(0,0)


state = 'idle'
rate = 2
phase = 0
amount_phases = 7
current_lights = [[[0,0,0]] * 100] * 7

file = os.getcwd() + '/LED_Patterns/'
idle_lights = read_blink_patern('idle')
los_lights = read_blink_patern('los/idle')
game_lights = read_blink_patern('game/idle')
win_lights = read_blink_patern('win/idle')

