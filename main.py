from machine import Pin
import time

LED_G = Pin(2, Pin.OUT)
LED_Y = Pin(3, Pin.OUT)
LED_R = Pin(4, Pin.OUT)

BUTTON = Pin(5, Pin.IN, Pin.PULL_UP)

segmentos = [
    Pin(28, Pin.OUT),  #A
    Pin(27, Pin.OUT),  #B
    Pin(26, Pin.OUT),  #C
    Pin(22, Pin.OUT),  #D
    Pin(21, Pin.OUT),  #E
    Pin(20, Pin.OUT),  #F
    Pin(19, Pin.OUT),  #G
]

numeros = {
    0: [1, 1, 1, 1, 1, 1, 0],
    1: [0, 1, 1, 0, 0, 0, 0],
    2: [1, 1, 0, 1, 1, 0, 1],
    3: [1, 1, 1, 1, 0, 0, 1],
    4: [0, 1, 1, 0, 0, 1, 1],
    5: [1, 0, 1, 1, 0, 1, 1],
    6: [1, 0, 1, 1, 1, 1, 1],
    7: [1, 1, 1, 0, 0, 0, 0],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 1, 1]
}


def mostrar_numero(numero):
    padrao = numeros[numero]

    for i in range(7):
        segmentos[i].value(padrao[i])
        

def apagar_display():

    for i in range(7):
        segmentos[i].value(0)


def semaforo_verde():
    apagar_display()

    LED_G.value(1)
    LED_R.value(0)
    LED_Y.value(0)

def semaforo_vermelho():
    LED_G.value(0)
    LED_R.value(1)
    LED_Y.value(0)

def semaforo_amarelo():
    LED_G.value(0)
    LED_R.value(0)
    LED_Y.value(1)

def piscar_led():
    time.sleep(0.2)
    apagar_display()
    time.sleep(0.2)
    mostrar_numero(contador)
    time.sleep(0.2)

# MAIN

while True:
    semaforo_verde()

    if BUTTON.value() == 0:
        time.sleep(5)
        semaforo_amarelo()
        time.sleep(3)

        semaforo_vermelho()
        
        for contador in range(9, 0, -1):
            mostrar_numero(contador)
            
            if contador < 5:
                piscar_led()
                piscar_led()             

            else:
                time.sleep(1)
        
