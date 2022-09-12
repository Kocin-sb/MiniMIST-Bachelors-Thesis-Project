from machine import Pin
import time

p = Pin(2, Pin.OUT)
p1 = Pin(12, Pin.OUT)
p2 = Pin(15, Pin.OUT) 

def toggle(max):
    lap = 0
    while (lap < max):
        p.value(1)
        p1.value(1)
        p2.value(1)
        time.sleep(1)
        p.value(0)
        p1.value(0)
        p2.value(0)
        time.sleep(1)  
        lap+=1

toggle(20)