import spidev
import ws2812
import time

spi = spidev.SpiDev()
spi.open(0,0)


current_lights = [[0,0,0]] * 100

def idle_():
    print("Leds are on")

#write 4 WS2812's, with the following colors: red, green, blue, yellow
ws2812.write2812(spi, current_lights)
