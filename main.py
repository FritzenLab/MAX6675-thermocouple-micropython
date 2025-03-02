# This code was modified by Clovis Fritzen, based on https://github.com/BetaRavener/micropython-hw-lib/tree/master/MAX6675
from max6675 import MAX6675
from machine import Pin
import time

so = Pin(18, Pin.IN)
sck = Pin(16, Pin.OUT)
cs = Pin(17, Pin.OUT)

max = MAX6675(sck, cs , so)
initialtime= time.ticks_ms() #https://docs.micropython.org/en/latest/library/time.html

while True:
    currenttime= time.ticks_ms() #Every time it passes here, gets the current time
    if time.ticks_diff(time.ticks_ms(), initialtime) > 1000: # this IF will be true every 1000 ms
        initialtime= time.ticks_ms() #update with the "current" time

        print(max.read())
    