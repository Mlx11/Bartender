# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 23:57:37 2020

@author: micha
"""
from config import *
import time
import RPi.GPIO as GPIO


class Pump:
    def __init__(self, name, gpio=0, sim=True):
        self.name = name
        self.on = False
        self.sim = sim
        # init gpio pin
        if not sim:
            self.gpio = gpio
            GPIO.setup(gpio, GPIO.OUT)
        

    def turn_on(self):
        self.on = True
        if not self.sim: 
            GPIO.output(self.gpio, GPIO.HIGH)

    def turn_off(self):
        self.on = False
        if not self.sim: 
            GPIO.output(self.gpio, GPIO.LOW)


    def __str__(self):
        if self.on:
            negator = ""
        else:
            negator = "not "
        return "{} is {} running".format(self.name, negator)

def wash():
    for key, pump in pumpes.items():
        pump.turn_on()
    time.sleep(10)
    for key, pump in pumpes:
        pump.turn_off()
        
def cleanup():
    GPIO.cleanup() # cleanup all GPIO


GPIO.setmode(GPIO.BCM) #name pins by gpio number (not pin number on the board)    

pumpes = {1: Pump("Pump 1", gpio=GPIO_PIN_NUMBERS[1], sim=False),
          2: Pump("Pump 2", gpio=GPIO_PIN_NUMBERS[2], sim=False),
          3: Pump("Pump 3", gpio=GPIO_PIN_NUMBERS[3], sim=False),
          4: Pump("Pump 4", gpio=GPIO_PIN_NUMBERS[4], sim=False),
          5: Pump("Pump 5", gpio=GPIO_PIN_NUMBERS[5], sim=False),
          6: Pump("Pump 6", gpio=GPIO_PIN_NUMBERS[6], sim=False),
          7: Pump("Pump 7", gpio=GPIO_PIN_NUMBERS[7], sim=False),
          8: Pump("Pump 8", gpio=GPIO_PIN_NUMBERS[8], sim=False),
          9: Pump("Pump 9", gpio=GPIO_PIN_NUMBERS[9], sim=False),
          10: Pump("Pump 10", gpio=GPIO_PIN_NUMBERS[10], sim=False),
          11: Pump("Pump 11", gpio=GPIO_PIN_NUMBERS[11], sim=False),
          12: Pump("Pump 12", gpio=GPIO_PIN_NUMBERS[12], sim=False)}
