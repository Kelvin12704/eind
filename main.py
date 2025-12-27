from apiotbord import led, start_up, potentio, temperature, knop1, knop2
from time import sleep

start_up()
while True:
    potValue = int(potentio()) 

    knop1_value = knop1().value()
    knop2_value = knop2().value()

    if 3 <= potValue <= 8:
        led(potValue).on()
        sleep(0.1)
        led(potValue).off()
        sleep(0.1)
        if potValue == 3 and knop1_value == 0:
            while True:
                for i in range(9):  #led 1 voor 1 aan
                    led(i).on()
                    sleep(0.1)
            
                for i in range(9): #led 1 voor 1 uit
                    led(i).off()
                    sleep(0.1)
                if knop2().value():
                    break