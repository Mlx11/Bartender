# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 22:08:19 2020

@author: micha
"""
import gui
import hardware
import time
import math

SECONDS_PER_MILILITER = 0.1
WASHING_TIME = 5

queue = []
pump_running = False
pump_stop_time = 0


# ------ Ingredients -----------------


def add_i1(ml):
    queue.append({"pump": 1, "volume": ml})  # <----------- 4. ingredient 1 is added to the queue - you don't have to do more


def add_i8(ml):
    queue.append({"pump": 8, "volume": ml})  # <----------- 5. ingredient 1 is added to the queue - you don't have to do more


# ---------- Drinks -----------------


def make_Drink1():
    add_i1(50)  # <------------- 3. 50ml of ingedient 1 is added
    add_i8(100)  # <------------- 4. 50ml of ingedient 8 is added


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
            time_to_run = next_element["volume"]*SECONDS_PER_MILILITER
            pump_stop_time = time.time() + time_to_run
            hardware.pumpes[pump_running].turn_on()
            print("Pump {} runs for {}s".format(pump_running, time_to_run))

    # washing
    if ui.washing:
        print("Start Washing, press stop to end")
        ui.washing = False
        for key, pump in hardware.pumpes.items():
            pump.turn_on()




if __name__ == "__main__":
    ui = gui.GUI()
