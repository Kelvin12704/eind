from machine import Pin, ADC
from time import sleep

def led(n): #define led 
    return Pin(n+1, Pin.OUT)

def start_up(): #define startup 
    for i in range(1, 8):
        led(i).on()
        sleep(0.1)
    for i in range(1, 8):
        led(i).off()
        sleep(0.1)