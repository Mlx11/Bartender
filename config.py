# -*- coding: utf-8 -*-

# Button Text
GUI_B1_TEXT = "Mojito"
GUI_B2_TEXT = "Strong Bull"
GUI_B3_TEXT = "Margarita"
GUI_B4_TEXT = "Californi- \n cation"
GUI_B5_TEXT = "Long Island"
GUI_B6_TEXT = "Vodka OJ"
GUI_B7_TEXT = "Gummibärli"
GUI_B8_TEXT = "Gin Tonic"
GUI_B9_TEXT = "Rum Cola"
GUI_B_STOP_TEXT = "STOP"
GUI_B_WASH_TEXT = "Wash"
GUI_CHECKBOX_WASH_TEXT = "Wash"
GUI_CHECKBOX_ACTIVATE_TEXT = "Activate"
GUI_DEACTIVATED_WARNING_TEXT = "The Bartender is deactivated"
GUI_DEACTIVATED_WINDOW_NAME = "Warning"
GUI_WASH_WARNING_TEXT = "Washing is deactivated"
GUI_WASH_WINDOW_NAME = "Warning"
GUI_CHECKBOX_SIMULATION_TEXT = "Show Sim"
# GUI Colors
GUI_BUTTON_BG_COLOR = "#CCCCCC"
GUI_BUTTON_STOP_BG_COLOR = "#FF0000"
GUI_BUTTON_WASH_BG_COLOR = "#888888"
GUI_SIM_BG = "#CC0000"
GUI_WINDOW_BG = "#000000"
ADDITIONAL_INFO_BG = "#CCCCCC"
GUI_SWITCHES_BACKGROUND = "#000000"


# Size
GUI_BUTTON_HEIGHT = 4
GUI_BUTTON_WIDTH = 10

# Information Text

DEFAULT_INFORMATION = {
    'Title': "Welcome",
    'Text': """ > Put your glass in the bartender \n > Choose your drink \n > Add a topping"""
    }
DRINK_INFORMATION = {1:{'Title': "Mojito", 'Text': "Toppings:mint,lime juice,lime, \n brown sugar,ice"},
                     2:{'Title': "Strong Bull", 'Text': "Topping:ice"},
                     3:{'Title': "Margarita", 'Text': "Toppings:ice"},
                     4:{'Title': "Californi-\ncation", 'Text': "Toppings:lime juice,ice"},
                     5:{'Title': "Long Island\nIced Tea", 'Text': "Toppings:ice"},
                     6:{'Title': "Vodka mit OJ", 'Text': "Toppings:ice \n Orange juice is healthy,\n that's all we care."},
                     7:{'Title': "Gummibärli", 'Text': "Toppings:ice"},
                     8:{'Title': "Gin Tonic", 'Text': "Toppings:ice"},
                     9:{'Title': "Rum Cola", 'Text': "Toppings:ice"}
                     }

#GPIO pins format: pump_nr : gpio number
# !!! the indicated gpio number is the name of the gpio and NOT THE HARDWARE PIN NUMBER
GPIO_PIN_NUMBERS = {
    1: 14,
    2: 15,
    3: 18,
    4: 23,
    5: 24,
    6: 25,
    7: 8,
    8: 7,
    9: 1,
    10: 12,
    11: 16,
    12: 20
    }


















