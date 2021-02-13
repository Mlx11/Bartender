# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 23:57:37 2020

@author: micha
"""

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
        
def init():
    GPIO.setmode(GPIO.BCM) #name pins by gpio number (not pin number on the board)
    



pumpes = {1: Pump("Pump 1", gpio=23, sim=False),
          2: Pump("Pump 2"),
          3: Pump("Pump 3"),
          4: Pump("Pump 4"),
          5: Pump("Pump 5"),
          6: Pump("Pump 6"),
          7: Pump("Pump 7"),
          8: Pump("Pump 8"),
          9: Pump("Pump 9"),
          10: Pump("Pump 10"),
          11: Pump("Pump 11"),
          12: Pump("Pump 12")}
