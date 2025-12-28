from apiotbord import led, start_up, potentio, temperature, knop1, knop2
from time import sleep

start_up()
while True:
    potValue = int(potentio()) 

    knop1_value = knop1().value()


    if 3 <= potValue <= 8: #limiteert de potentiemeter 
        led(potValue).on()
        sleep(0.1)
        led(potValue).off()
        sleep(0.1)
    
        elif potValue == 3 and knop1_value == 0: #selecteren programma 1
            while True:
                # Stop direct als knop2 wordt ingedrukt
                knop2_value = knop2().value()
                if knop2_value == 0:
                    break

                # LED loopt vooruit van 1 naar 8
                for i in range(1, 8 + 1):
                    led(i).on()
                    sleep(0.1)
                    led(i).off()
                    

               # LED loopt achteruit van 8 naar 1
                for i in reversed(range(1, 8 + 1)):
                    led(i).on()
                    sleep(0.1)
                    led(i).off()

        
                if knop2_value == 0: #stopt programma
                    break

        
                sleep(1)  # korte pauze tussen loops

        if potValue == 4 and knop1_value == 0: #selecteren programma 2
            while True:
                for i in range(9):  #led 1 voor 1 aan
                    led(i).on()
                    sleep(0.1)
            
                for i in range(9): #led 1 voor 1 uit
                    led(i).off()
                    sleep(0.1)

                knop2_value = knop2().value()
                if knop2_value == 0: #stopt programma
                    break
