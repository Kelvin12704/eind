from apiotbord import led, start_up, potentio, temp, knop1, knop2, led1, led2, led3, led4, led5, led6, led7, led8
from time import sleep
import random


start_up()
while True:
    potValue = int(potentio()) 

    knop1_value = knop1().value()


    if 3 <= potValue <= 8: #limiteert de potentiemeter 
        led(potValue).on()
        sleep(0.1)
        led(potValue).off()
        sleep(0.1)
    
    if potValue == 3 and knop1_value == 0: #selecteren programma 1
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

    elif potValue == 4 and knop1_value == 0: #selecteren programma 2
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
    elif potValue == 5 and knop1_value == 0:  # Programma 4
        while True:
            if knop1().value() == 0: #knop 1 indrukken om te gooien
                getal = random.randint(1, 6)
                
                for i in range(1,9): #alle leds gaan uit
                    led(i).off()
                
                if getal == 1:
                    led(3).on()
                elif getal == 2:
                    led(3).on(); led(4).on()
                elif getal == 3:
                    led(3).on(); led(4).on(); led(5).on()
                elif getal == 4:
                    led(3).on(); led(4).on(); led(5).on(); led(6).on()
                elif getal == 5:
                    led(3).on(); led(4).on(); led(5).on(); led(6).on(); led(7).on()
                elif getal == 6:
                    led(3).on(); led(4).on(); led(5).on(); led(6).on(); led(7).on(); led(8).on()
                
            knop2_value = knop2().value()
            if knop2_value == 0: #stopt programma
                for i in range(1, 9):    
                    led(i).off()
                break

    elif potValue == 6 and knop1_value == 0: #selecteren programma 4
        while True:
            temperature = temp()
            print("Temp:", temperature) #test uitgaandee waarde
            sleep(1)
            if temperature > -10 and temperature < 0: #tussen -10 en 0 graden gaat led 1 aan
                led1.on()
                sleep(0.1)
                led1.off()
            if temperature >= 0 and temperature < 5: #tussen 0 en 5 graden gaat led 2 aan 
                led2.on()
                sleep(0.1)
                led2.off()
            if temperature >= 5 and temperature < 10: #enz...
                led3.on()
                sleep(0.1)
                led3.off()
            if temperature >= 10 and temperature < 15:
                led4.on()
                sleep(0.1)
                led4.off()
            if temperature >= 15 and temperature < 20:
                led5.on()
                sleep(0.1)
                led5.off()
            if temperature >= 20 and temperature < 25:
                led6.on()
                sleep(0.1)
                led6.off()
            if temperature >= 25 and temperature < 30:
                led7.on()
                sleep(0.1)
                led7.off()
            if temperature >= 30 and temperature < 35:
                led8.on()
                sleep(0.1)
                led8.off()
            
            knop2_value = knop2().value()
            if knop2_value == 0: #stopt programma
                break
    elif potValue == 7 and knop1_value == 0: #programma 5
        BESTAND = "getal.txt"
     
        while True:
            try:
                # Getal lezen uit bestand
                with open(BESTAND, "r") as f: #lees het bestand
                    aantal = int(f.read())

                # Beveiliging: alleen 1 t.e.m. 8
                if aantal < 1:
                    aantal = 1
                if aantal > 8:
                    aantal = 8

            except:
                # Als bestand niet bestaat of fout is
                aantal = 0

            for i in range(1, 9):
                led(i).off()

            for i in range(1, aantal + 1):
                led(i).on()

            sleep(1)
            
            knop2_value = knop2().value()
            if knop2_value == 0: #stopt het prograama
                led(i).off()
                break