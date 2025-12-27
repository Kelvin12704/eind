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

def potentio():
    """Return the potentiometer value"""
    potentiometer = ADC(28)
    potentiometer_value = potentiometer.read_u16()/8000
    return potentiometer_value

def temperature():
    """Return the temperature value"""
    temperature_sensor = ADC(4)
    temperature_value = temperature_sensor.read_u16()
    volt = (3.3/65535)*temperature_value
    temperature = 27 - (volt - 0.706)/0.001721
    return round(temperature, 1)  
 
def knop1():
    knp1 = Pin(22, Pin.IN, pull=Pin.PULL_UP)
    return knp1

def knop2():
    knp2 = Pin(10, Pin.IN, pull=Pin.PULL_UP)
    return knp2