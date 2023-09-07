import spidev
import ws2812
import time
import os
import csv

def blink():
    global state
    global phase
    phase = 0
    while True:
        if state == 'idle':
                current_lights = idle_lights [phase]
        elif state ==  'win':
                current_lights = win_lights [phase]
        elif state ==  'los':
                current_lights = los_lights [phase]
        elif state == 'game':   
                current_lights = game_lights [phase]
        phase = (phase + 1) % phase_dict[state]
        ws2812.write2812(spi, current_lights)
        time.sleep(rate_dict[state])

def set_led_state (new_state):
    global state
    global phase
    phase = 0
    state = new_state

def read_blink_patern(file_name):
        result = []
        for i in range(phase_dict[file_name]):
                phase = []
                with open( os.getcwd() + '/LED_Patterns/' + file_name + '/phase' + str(i + 1) + '.csv', mode='r') as csv_file:
                        # Create a CSV reader object
                        csv_reader = csv.reader(csv_file)
    
                        # Loop through each row in the CSV file
                        for row in csv_reader:
                                # Convert each item in the row to an integer and append it to the list
                                phase.append([int(item) for item in row])
                result.append(phase)
        return result


spi = spidev.SpiDev()
spi.open(0,0)


state = 'idle'
phase = 0
amount_phases = 7
current_lights = [[[0,0,0]] * 100] * 7


phase_dict = {'idle' : 4, 'game' : 4, 'win' : 2, 'los' : 2}
rate_dict = {'idle' : 1, 'game' : 0.25, 'win' : 1, 'los' : 1}

file = os.getcwd() + '/LED_Patterns/'
idle_lights = read_blink_patern('idle')
los_lights = read_blink_patern('los')
game_lights = read_blink_patern('game')
win_lights = read_blink_patern('win')
