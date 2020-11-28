# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:06:02 2020

@author: micha
"""
import tkinter as tk
import main
import hardware

DEBUG = False # show debug messages if true
SIMULATION = True # shows simulations for the pumps


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.build_gui()
        self.window.after(200, self.task)
        self.window.after(1000, self.update_pump_simulation)
        self.button_pressed = [False]*8
        self.button_stop_pressed = False
        self.window.mainloop()


    def build_gui(self):
        # background color
        self.window.configure(bg="#571F4E")

        #create widgets
        # buttons
        button1 = tk.Button(self.window, text="Drink 1", command=lambda: self.on_button_pressed(1), bg="#A2FAA3", width=20, height=8)
        button2 = tk.Button(self.window, text="Drink 2", command=lambda: self.on_button_pressed(2), bg="#92C9B1", width=20, height=8)
        button3 = tk.Button(self.window, text="Drink 3", command=lambda: self.on_button_pressed(3), bg="#4F759B", width=20, height=8)
        button4 = tk.Button(self.window, text="Drink 4", command=lambda: self.on_button_pressed(4), bg="#5D5179", width=20, height=8)
        button5 = tk.Button(self.window, text="Drink 5", command=lambda: self.on_button_pressed(5), bg="#A2FAA3", width=20, height=8)
        button6 = tk.Button(self.window, text="Drink 6", command=lambda: self.on_button_pressed(6), bg="#92C9B1", width=20, height=8)
        button7 = tk.Button(self.window, text="Drink 7", command=lambda: self.on_button_pressed(7), bg="#4F759B", width=20, height=8)
        button8 = tk.Button(self.window, text="Drink 8", command=lambda: self.on_button_pressed(8), bg="#5D5179", width=20, height=8)
        button_stop = tk.Button(self.window, text ="Stop", command=self.on_button_stop_pressed, bg="#999999", width=20, height=8)
        #pump simulation
        frame = tk.Frame(self.window, bg="#571F4E")
        self.pump_label1 = tk.Label(frame,text="Pump 1", bg="#FF0000")
        self.pump_label2 = tk.Label(frame,text="Pump 2", bg="#FF0000")
        self.pump_label3 = tk.Label(frame,text="Pump 3", bg="#FF0000")
        self.pump_label4 = tk.Label(frame,text="Pump 4", bg="#FF0000")
        self.pump_label1.pack()
        self.pump_label2.pack()
        self.pump_label3.pack()
        self.pump_label4.pack()
        # grid layout
        button1.grid(row=0, column=0, padx='5', pady='5', sticky='ew')
        button2.grid(row=1, column=0, padx='5', pady='5', sticky='ew')
        button3.grid(row=1, column=1, padx='5', pady='5', sticky='ew')
        button4.grid(row=0, column=1, padx='5', pady='5', sticky='ew')
        button5.grid(row=2, column=0, padx='5', pady='5', sticky='ew')
        button6.grid(row=3, column=0, padx='5', pady='5', sticky='ew')
        button7.grid(row=2, column=1, padx='5', pady='5', sticky='ew')
        button8.grid(row=3, column=1, padx='5', pady='5', sticky='ew')
        button_stop.grid(row=3, column=3, padx='5', pady='5', sticky='ew')
        frame.grid(row=0, column=3, padx='5', pady='5', sticky='ew')

    def on_button_pressed(self, i):
        self.button_pressed[i-1] = True
        if DEBUG:
            print("Button {} pressed".format(i))

    def on_button_stop_pressed(self):
        self.button_stop_pressed = True
        if DEBUG:
            print("Button stop pressed")

    def button_was_pressed(self, nr):
        res = self.button_pressed[nr-1]
        self.button_pressed[nr-1] = False
        return res

    def stop_was_pressed(self):
        res =  self.button_stop_pressed
        self.button_stop_pressed = False
        return res
    
    def update_pump_simulation(self):
        if hardware.pumpes[1].on:
            self.pump_label1.configure(bg="#00FF00")
        else:
            self.pump_label1.configure(bg="#FF0000")
        if hardware.pumpes[2].on:
            self.pump_label2.configure(bg="#00FF00")
        else:
            self.pump_label2.configure(bg="#FF0000")
        if hardware.pumpes[3].on:
            self.pump_label3.configure(bg="#00FF00")
        else:
            self.pump_label3.configure(bg="#FF0000")
        if hardware.pumpes[4].on:
            self.pump_label4.configure(bg="#00FF00")
        else:
            self.pump_label4.configure(bg="#FF0000")
        self.window.after(1000, self.update_pump_simulation)


    def task(self):
        main.main(self)
        self.window.after(200, self.task)
        



if __name__ == "__main__":
    gui = GUI()






