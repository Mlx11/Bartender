# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 23:57:37 2020

@author: micha
"""

class Pump:
    def __init__(self, name):
        self.name = name
        self.on = False

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def __str__(self):
        if self.on:
            negator = ""
        else:
            negator = "not "
        return "{} is {} running".format(self.name, negator)
    

pumpes = {1:Pump("Pump 1"), 2:Pump("Pump 2"), 3:Pump("Pump 3"), 4:Pump("Pump 4")}