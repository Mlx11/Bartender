# -*- coding: utf-8 -*-

# Button Text
GUI_B1_TEXT = "Drink1"
GUI_B2_TEXT = "Drink2"
GUI_B3_TEXT = "Drink3"
GUI_B4_TEXT = "Drink4"
GUI_B5_TEXT = "Drink5"
GUI_B6_TEXT = "Drink6"
GUI_B7_TEXT = "Drink7"
GUI_B8_TEXT = "Drink8"
GUI_B9_TEXT = "Drink9"
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
ADDITIONAL_INFO_BG = "#FFFFFF"
GUI_SWITCHES_BACKGROUND = "#000000"


# Size
GUI_BUTTON_HEIGHT = 3
GUI_BUTTON_WIDTH = 6

# Information Text

DEFAULT_INFORMATION = {
    'Title': "Welcome",
    'Text': """ > Put your glass in the bartender \n > Choose your drink \n > Add a toping"""
    }
DRINK_INFORMATION = {1:{'Title': "Drink 1", 'Text': "This is a placeholder for the description \n This tests a new line"},
                     2:{'Title': "Drink 2", 'Text': "Text 2"},
                     3:{'Title': "Drink 2", 'Text': "Text 2"},
                     4:{'Title': "Drink 2", 'Text': "Text 2"},
                     5:{'Title': "Drink 2", 'Text': "Text 2"},
                     6:{'Title': "Drink 2", 'Text': "Text 2"},
                     7:{'Title': "Drink 2", 'Text': "Text 2"},
                     8:{'Title': "Drink 2", 'Text': "Text 2"},
                     9:{'Title': "Drink 2", 'Text': "Text 2"}
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


















