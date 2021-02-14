# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 22:08:19 2020

@author: micha
"""
import gui
import hardware
import time
import math
import traceback
import sys

SECONDS_PER_MILILITER = 0.02
CONSTANT_START_TIME = 1

queue = []
pump_running = False
pump_stop_time = 0


# ------ Ingredients -----------------


def add_i1(ml):# <-------Vodka
    queue.append({"pump": 1, "volume": ml}) 

def add_i2(ml):# <-------Weisser Rum
    queue.append({"pump": 2, "volume": ml})

def add_i3(ml):# <-------Tequila
    queue.append({"pump": 3, "volume": ml})

def add_i4(ml):# <-------Triple Sec
    queue.append({"pump": 4, "volume": ml})

def add_i5(ml):# <-------Gin
    queue.append({"pump": 5, "volume": ml})

def add_i6(ml):# <-------Cola
    queue.append({"pump": 6, "volume": ml})

def add_i7(ml):# <-------OJ
    queue.append({"pump": 7, "volume": ml})

def add_i8(ml):# <-------Cointreau
    queue.append({"pump": 8, "volume": ml}) 

def add_i9(ml):# <-------Energy Drink
    queue.append({"pump": 9, "volume": ml}) 

def add_i10(ml):# <-------Tonic Water
    queue.append({"pump": 10, "volume": ml}) 
    
def add_i11(ml):# <-------Energy Drink
    queue.append({"pump": 11, "volume": ml}) 

def add_i12(ml):# <-------Tonic Water
    queue.append({"pump": 12, "volume": ml}) 
    
# ---------- Drinks -----------------


def make_Drink1(): #Mojito
    add_i2(50)  # <------------- 3. 50ml of ingedient 1 is added     

def make_Drink3(): #Margarita
    add_i8(10)  # <------------- 3. 50ml of ingedient 1 is added 
    add_i3(30)
    
def make_Drink4(): #Californication
    add_i1(15)  # <------------- 3. 50ml of ingedient 1 is added 
    add_i5(15)
    add_i2(15)
    add_i3(15)
    add_i7(70)

def make_Drink5(): #Long Island Iced Tea
    add_i2(20)  # <------------- 3. 50ml of ingedient 1 is added 
    add_i1(20)
    add_i5(20)
    add_i3(20)
    add_i4(20)
    add_i6(50)
    
def make_Drink6(): #Vodka mit OJ
    add_i1(50)  # <------------- 3. 50ml of ingedient 1 is added 
    add_i7(250) # <-------------Attention 150ml raised
    
def make_Drink7(): #Gummibärli
    add_i1(50)  # <------------- 3. 50ml of ingedient 1 is added 
    add_i9(100)
    
def make_Drink8(): #Gin Tonic
    add_i5(50)  # <------------- 3. 50ml of ingedient 1 is added 
    add_i10(250) # <-----------Attention 150ml raised
    
def make_Drink9(): #Rum Cola
    add_i2(50)  # <------------- 3. 50ml of ingedient 1 is added 
    add_i6(100)
    
def make_Drink10(): #Strong Bull
    add_i2(50)  # <------------- 3. 50ml of ingedient 1 is added 
    add_i9(100)

# ---------- main -------------------

def main(ui):
    global pump1, queue, pump_running, pump_stop_time
    if ui.stop_was_pressed():
        # stop all the punps, reset the queue
        print("stop button was pressed")
        for key, pump in hardware.pumpes.items():
            pump.turn_off()
        queue = []
        ui.washing = False
        washing_stop_time = pow(10,10)
        return

    if ui.button_was_pressed(1):  # <--------- 1. When button 1 was pressed
        print("button 1 was pressed")
        make_Drink1()  # <-------------------- 2. the function make_drink1 is called
    elif ui.button_was_pressed(2):
        print("button 2 was pressed")
        make_Drink1() # !!!!!!!!!!!!!!!!!!!¨not drink 2
    elif ui.button_was_pressed(3):
        print("button 3 was pressed")
        make_Drink3()
    elif ui.button_was_pressed(4):
        print("button 4 was pressed")
        make_Drink4()
    elif ui.button_was_pressed(5):
        print("button 5 was pressed")
        make_Drink5()
    elif ui.button_was_pressed(6):
        print("button 6 was pressed")
        make_Drink6()
    elif ui.button_was_pressed(7):
        print("button 7 was pressed")
        make_Drink7()
    elif ui.button_was_pressed(8):
        print("button 8 was pressed")
        make_Drink8()
    elif ui.button_was_pressed(9):
        print("button 8 was pressed")
        make_Drink9()

    # check the queue, stop/start pumps
    if pump_running:
        ui.text_time_left.set(str(int(pump_stop_time - time.time())))
        if pump_stop_time <= time.time():
            hardware.pumpes[pump_running].turn_off()
            pump_running = False
            time_to_run = 0
    else:
        if len(queue) != 0:
            next_element = queue[0]
            queue = queue[1:]
            pump_running = next_element["pump"]
            time_to_run = next_element["volume"]*SECONDS_PER_MILILITER + CONSTANT_START_TIME
            pump_stop_time = time.time() + time_to_run
            hardware.pumpes[pump_running].turn_on()
            print("Pump {} runs for {}s".format(pump_running, time_to_run))

    # washing
    if ui.washing:
        print("Start Washing")
        ui.washing = False
        add_i1(500)
        add_i2(500)
        add_i3(500)
        add_i4(500)
        add_i5(500)
        add_i6(500)
        add_i7(500)
        add_i8(500)
        add_i9(500)
        add_i10(500)
        add_i11(500)
        add_i12(500)




if __name__ == "__main__":
    try:
        ui = gui.GUI()
    except Exception:
        traceback.print_stack()
    finally: 
        hardware.cleanup()
    
    
    
    
    
