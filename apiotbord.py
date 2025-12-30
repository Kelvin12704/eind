from machine import Pin, ADC
from time import sleep


def led(n): #define led 
    return Pin(n+1, Pin.OUT)

def start_up():
    for _ in range(5):
        for i in range(9):
            led(i).on()
        sleep(0.1)

        for i in range(9):
            led(i).off()
        sleep(0.1)


def potentio():
    """Return the potentiometer value"""
    potentiometer = ADC(28)
    potentiometer_value = potentiometer.read_u16()/8000
    return potentiometer_value



def temp():
    temp_sensor = ADC(4)
    adc_value = temp_sensor.read_u16()
    voltage = adc_value * 3.0 / 65535
    return 27 - ((voltage - 0.706) / 0.001721)

  
 
def knop1():
    knp1 = Pin(22, Pin.IN, pull=Pin.PULL_UP)
    return knp1

def knop2():
    knp2 = Pin(10, Pin.IN, pull=Pin.PULL_UP)
    return knp2

def led1():
    led1 = Pin(2, Pin.OUT)
    return led1
    
def led2():
    led2 = Pin(3, Pin.OUT)
    return led2

def led3():
    led1 = Pin(4, Pin.OUT)
    return led3

def led4():
    led4 = Pin(5, Pin.OUT)
    return led4

def led5():
    led5 = Pin(6, Pin.OUT)
    return led5

def led6():
    led6 = Pin(7, Pin.OUT)
    return led6

def led7():
    led7 = Pin(8, Pin.OUT)
    return led7

def led8():
    led8 = Pin(9, Pin.OUT)
    return led8