# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 22:08:19 2020

@author: micha
"""
import gui
import hardware
import time

def main(ui):
    global pump1
    if ui.stop_was_pressed():
        print("stop button was pressed")
        hardware.pumpes[1].turn_off()
        hardware.pumpes[2].turn_off()
        hardware.pumpes[3].turn_off()
        hardware.pumpes[4].turn_off()
    if ui.button_was_pressed(1):
        print("button 1 was pressed")
        hardware.pumpes[1].turn_on()
    elif ui.button_was_pressed(2):
        print("button 2 was pressed")
        hardware.pumpes[2].turn_on()
    elif ui.button_was_pressed(3):
        print("button 3 was pressed")
        hardware.pumpes[3].turn_on()
    elif ui.button_was_pressed(4):
        print("button 4 was pressed")
        hardware.pumpes[4].turn_on()
    elif ui.button_was_pressed(5):
        print("button 5 was pressed")
    elif ui.button_was_pressed(6):
        print("button 6 was pressed")
    elif ui.button_was_pressed(7):
        print("button 7 was pressed")
    elif ui.button_was_pressed(8):
        print("button 8 was pressed")


if __name__ == "__main__":
    ui = gui.GUI()
