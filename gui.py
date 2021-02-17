# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:06:02 2020

@author: michel & raphael
"""
import tkinter as tk
import tkinter.font
import main
import hardware
from config import *

DEBUG = True # show debug messages if true
SIMULATION = True # shows simulations for the pumps


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.grid_rowconfigure(0, weight=1) # this and the next line allow filling a grid layout
        self.window.grid_columnconfigure(0, weight=1)
        self.build_gui()
        self.window.after(200, self.task)
        self.window.after(1000, self.update_pump_simulation)
        self.button_pressed = [False]*9
        self.button_stop_pressed = False
        self.washing = False

        self.window.mainloop()


    def build_gui(self):
        # background color
        self.window.configure(bg=GUI_WINDOW_BG) # window background
        self.button_font = tk.font.Font(family='Helvetica', size=12, weight='bold')


        #create widgets
        # buttons
        button1 = tk.Button(self.window, text=GUI_B1_TEXT, command=lambda: self.on_button_pressed(1), bg=GUI_BUTTON_BG_COLOR, width=GUI_BUTTON_WIDTH, height=GUI_BUTTON_HEIGHT)
        button2 = tk.Button(self.window, text=GUI_B2_TEXT, command=lambda: self.on_button_pressed(2), bg=GUI_BUTTON_BG_COLOR, width=GUI_BUTTON_WIDTH, height=GUI_BUTTON_HEIGHT)
        button3 = tk.Button(self.window, text=GUI_B3_TEXT, command=lambda: self.on_button_pressed(3), bg=GUI_BUTTON_BG_COLOR, width=GUI_BUTTON_WIDTH, height=GUI_BUTTON_HEIGHT)
        button4 = tk.Button(self.window, text=GUI_B4_TEXT, command=lambda: self.on_button_pressed(4), bg=GUI_BUTTON_BG_COLOR, width=GUI_BUTTON_WIDTH, height=GUI_BUTTON_HEIGHT)
        button5 = tk.Button(self.window, text=GUI_B5_TEXT, command=lambda: self.on_button_pressed(5), bg=GUI_BUTTON_BG_COLOR, width=GUI_BUTTON_WIDTH, height=GUI_BUTTON_HEIGHT)
        button6 = tk.Button(self.window, text=GUI_B6_TEXT, command=lambda: self.on_button_pressed(6), bg=GUI_BUTTON_BG_COLOR, width=GUI_BUTTON_WIDTH, height=GUI_BUTTON_HEIGHT)
        button7 = tk.Button(self.window, text=GUI_B7_TEXT, command=lambda: self.on_button_pressed(7), bg=GUI_BUTTON_BG_COLOR, width=GUI_BUTTON_WIDTH, height=GUI_BUTTON_HEIGHT)
        button8 = tk.Button(self.window, text=GUI_B8_TEXT, command=lambda: self.on_button_pressed(8), bg=GUI_BUTTON_BG_COLOR, width=GUI_BUTTON_WIDTH, height=GUI_BUTTON_HEIGHT)
        button9 = tk.Button(self.window, text=GUI_B9_TEXT, command=lambda: self.on_button_pressed(9), bg=GUI_BUTTON_BG_COLOR, width=GUI_BUTTON_WIDTH, height=GUI_BUTTON_HEIGHT)

        button_stop = tk.Button(self.window, text =GUI_B_STOP_TEXT, command=self.on_button_stop_pressed, bg=GUI_BUTTON_STOP_BG_COLOR, width=GUI_BUTTON_WIDTH, height=GUI_BUTTON_HEIGHT)
        button_wash = tk.Button(self.window, text =GUI_B_WASH_TEXT, command=self.on_button_wash_pressed, bg=GUI_BUTTON_WASH_BG_COLOR, width=GUI_BUTTON_WIDTH, height=GUI_BUTTON_HEIGHT)
        
        button1['font'] = self.button_font
        button2['font'] = self.button_font
        button3['font'] = self.button_font
        button4['font'] = self.button_font
        button5['font'] = self.button_font
        button6['font'] = self.button_font
        button7['font'] = self.button_font
        button8['font'] = self.button_font
        button9['font'] = self.button_font
        button_stop['font'] = self.button_font
        button_wash['font'] = self.button_font

        #pump simulation
        self.frame = tk.Frame(self.window, bg=GUI_SIM_BG)
        self.pump_label1 = tk.Label(self.frame, text="Pump 1", bg="#FF0000", width=10)
        self.pump_label2 = tk.Label(self.frame, text="Pump 2", bg="#FF0000", width=10)
        self.pump_label3 = tk.Label(self.frame, text="Pump 3", bg="#FF0000", width=10)
        self.pump_label4 = tk.Label(self.frame, text="Pump 4", bg="#FF0000", width=10)
        self.pump_label5 = tk.Label(self.frame, text="Pump 5", bg="#FF0000", width=10)
        self.pump_label6 = tk.Label(self.frame, text="Pump 6", bg="#FF0000", width=10)
        self.pump_label7 = tk.Label(self.frame, text="Pump 7", bg="#FF0000", width=10)
        self.pump_label8 = tk.Label(self.frame, text="Pump 8", bg="#FF0000", width=10)
        self.pump_label9 = tk.Label(self.frame, text="Pump 9", bg="#FF0000", width=10)
        self.pump_label10 = tk.Label(self.frame, text="Pump 10", bg="#FF0000", width=10)
        self.pump_label11 = tk.Label(self.frame, text="Pump 11", bg="#FF0000", width=10)
        self.pump_label12 = tk.Label(self.frame, text="Pump 12", bg="#FF0000", width=10)
        self.text_time_left = tk.StringVar()
        self.text_time_left.set("all off")
        self.pump_run_time_label = tk.Label(self.window,textvariable=self.text_time_left , bg="#571F4E")
        self.pump_label1.pack()
        self.pump_label2.pack()
        self.pump_label3.pack()
        self.pump_label4.pack()
        self.pump_label5.pack()
        self.pump_label6.pack()
        self.pump_label7.pack()
        self.pump_label8.pack()
        self.pump_label9.pack()
        self.pump_label10.pack()
        self.pump_label11.pack()
        self.pump_label12.pack()
        
        # Information Text
        self.additional_info_frame = tk.Frame(self.window, bg=ADDITIONAL_INFO_BG)
        self.info_title_text = tk.StringVar()
        self.info_title_label = tk.Label(self.additional_info_frame, textvariable=self.info_title_text, anchor="nw", justify=tk.LEFT)
        self.info_title_label.config(font=("Courier", 30, "bold"))
        self.info_title_label.pack()
        self.info_title_text.set(DEFAULT_INFORMATION['Title'])
        
        self.info_content_text = tk.StringVar()
        self.info_content_label = tk.Label(self.additional_info_frame, textvariable=self.info_content_text, anchor="nw", justify=tk.LEFT)
        self.info_content_label.pack(side = tk.LEFT, expand=1, fill=tk.BOTH)
        self.info_content_text.set(DEFAULT_INFORMATION['Text'])



        
        #Switches
        self.wash_switch_var = tk.IntVar()
        self.activate_switch_var = tk.IntVar()
        self.simulation_switch_var = tk.IntVar()

        switch_frame = tk.Frame(self.window, bg=GUI_SWITCHES_BACKGROUND)
        wash_switch = tk.Checkbutton(switch_frame, text=GUI_CHECKBOX_WASH_TEXT, variable=self.wash_switch_var)
        deactivate_switch = tk.Checkbutton(switch_frame, text=GUI_CHECKBOX_ACTIVATE_TEXT, variable = self.activate_switch_var)
        simulation_switch = tk.Checkbutton(switch_frame, text=GUI_CHECKBOX_SIMULATION_TEXT, variable = self.simulation_switch_var)

        
        wash_switch.grid(row=0, column=0, padx='5', pady='5', sticky='ew')
        deactivate_switch.grid(row=1, column=0, padx='5', pady='5', sticky='ew')
        simulation_switch.grid(row=2, column=0, padx='5', pady='5', sticky='ew')


        
        # grid layout
        button1.grid(row=0, column=0, padx='5', pady='5', sticky='ew')
        button2.grid(row=0, column=1, padx='5', pady='5', sticky='ew')
        button3.grid(row=0, column=2, padx='5', pady='5', sticky='ew')
        button4.grid(row=1, column=0, padx='5', pady='5', sticky='ew')
        button5.grid(row=1, column=1, padx='5', pady='5', sticky='ew')
        button6.grid(row=1, column=2, padx='5', pady='5', sticky='ew')
        button7.grid(row=2, column=0, padx='5', pady='5', sticky='ew')
        button8.grid(row=2, column=1, padx='5', pady='5', sticky='ew')
        button9.grid(row=2, column=2, padx='5', pady='5', sticky='ew')

        button_stop.grid(row=2, column=3, padx='5', pady='5', sticky='ew')
        button_wash.grid(row=2, column=4, padx='5', pady='5', sticky='ew')
        self.frame.grid(row=0, column=5, padx='5', pady='5', sticky='ew', rowspan=2)
        switch_frame.grid(row=2, column=5, padx='5', pady='5', sticky='ew')
        #self.pump_run_time_label.grid(row=0, column=3, sticky='ew')
        self.additional_info_frame.grid(row=0, column=3, rowspan=2, columnspan=2, sticky="nsew", padx='5', pady='5')

    def on_button_pressed(self, i):
        self.info_content_text.set(DRINK_INFORMATION[i]['Text'])
        self.info_title_text.set(DRINK_INFORMATION[i]['Title'])
        if self.activate_switch_var.get():
            self.button_pressed[i-1] = True

            if DEBUG:
                print("Button {} pressed".format(i))
                print("Wash: ", self.wash_switch_var.get())
                print("Active: ", self.activate_switch_var.get())
    
    def on_button_wash_pressed(self):
        if self.wash_switch_var.get():
            self.washing = True
        else:
            tk.messagebox.showinfo(GUI_WASH_WINDOW_NAME, GUI_WASH_WARNING_TEXT)

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
        if hardware.pumpes[5].on:
            self.pump_label5.configure(bg="#00FF00")
        else:
            self.pump_label5.configure(bg="#FF0000")
        if hardware.pumpes[6].on:
            self.pump_label6.configure(bg="#00FF00")
        else:
            self.pump_label6.configure(bg="#FF0000")
        if hardware.pumpes[7].on:
            self.pump_label7.configure(bg="#00FF00")
        else:
            self.pump_label7.configure(bg="#FF0000")
        if hardware.pumpes[8].on:
            self.pump_label8.configure(bg="#00FF00")
        else:
            self.pump_label8.configure(bg="#FF0000")
        if hardware.pumpes[9].on:
            self.pump_label9.configure(bg="#00FF00")
        else:
            self.pump_label9.configure(bg="#FF0000")
        if hardware.pumpes[10].on:
            self.pump_label10.configure(bg="#00FF00")
        else:
            self.pump_label10.configure(bg="#FF0000")
        if hardware.pumpes[11].on:
            self.pump_label11.configure(bg="#00FF00")
        else:
            self.pump_label11.configure(bg="#FF0000")
        if hardware.pumpes[12].on:
            self.pump_label12.configure(bg="#00FF00")
        else:
            self.pump_label12.configure(bg="#FF0000")
            
        if (not self.simulation_switch_var.get()):
            self.frame.grid_remove()
        else:
            self.frame.grid()

        self.window.after(1000, self.update_pump_simulation)


    def task(self):
        main.main(self)
        self.window.after(200, self.task)
        



if __name__ == "__main__":
    gui = GUI()






