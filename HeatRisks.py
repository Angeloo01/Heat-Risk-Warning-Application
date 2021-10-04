# GlobalWarmingRisks.py
# All imports
from tkinter import colorchooser
import PySimpleGUI as PSG
import os.path
from HeatIndexData import get_risk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
from PySimpleGUI.PySimpleGUI import HorizontalSeparator
import requests
from bs4 import BeautifulSoup
from Useful import *
Calgary = (94, 55)

# Creating the layout for the Window
PSG.theme('DarkGrey14')
firstColumn = [
    # Text
    [PSG.Text("Please pick the city you would like to view data for:",
              font='Lucida', size=(40, 1))],
    # Dropdown Menu
    [PSG.Combo(['Amsterdam', 'Ankara', 'Athens', 'Baku', 'Bangkok', 'Barcelona', 'Berlin', 'Bern', 'Bogota', 'Bucharest', 'Buenos Aires', 'Cairo', 'Calgary', 'Canberra', 'Cape Town', 'Copn Hagen', 'Delhi', 'Doha', 'Dubai', 'Helsinki', 'Islamabad', 'Istanbul', 'Jakarta', 'Kabul', 'Kuala Lampur', 'Lisbon', 'London', 'Los Angeles', 'Madrid', 'Manila', 'Mexico City', 'Monaco', 'Moscow',  'New York City', 'Oslo', 'Paris', 'Perth', 'Rome', 'Sarajevo',  'Sao Paulo', 'Shanghai',  'Singapore', 'St.Petersburg', 'Taipei', 'Tokyo', 'Toronto', 'Vienna', 'Wellington'],
               enable_events=True, key='CityChosen', font='Lucida', size=(30, 1))],
]
dataAnalysisColumn = [
    # Text
    [PSG.Text("Here is some weather data for the city you chose, and the associated heat risks",
              font='Lucida', size=(40, -1))],
    [PSG.Text(size=(40, None), font='Lucida', key="-Results-")]
]
# Setting the layout, first Column is drop down menu, second column is graph viewer
layout = [
    [
        PSG.Column(firstColumn),
        PSG.VSeparator(),
        PSG.Column(dataAnalysisColumn)
    ]
]
# Creating the Window
window = PSG.Window("Heat Risks", layout)


# Main event loop, program loops forever until window is closed
while True:
    event, values = window.read()
    # If window is closed, break
    if event == PSG.WIN_CLOSED:
        break
    city = values['CityChosen']
    city = city+" weather"
    Weather.set_city(city)
    temp = (int(Weather.temperature) * 9/5) + 32
    percent_sign = Weather.humidity.find('%')
    Weather.humidity = Weather.humidity[0: percent_sign]
    if range_checker(temp, float(Weather.humidity)) == -1:
        status = -1
    elif range_checker(temp, float(Weather.humidity)) == -2:
        status = -2
    else:
        status = get_risk(temp, float(Weather.humidity))
    heatMessage = riskLevel(status)
    hello = ("For the city of: " +
             values['CityChosen'] + "\n\nTemparature\n----------------------\n" + str(Weather.temperature) + "°C" + "\n\nHumidity\n----------------------\n" + str(Weather.humidity) + "%" + "\n\nHeat Risk\n----------------------\n" + heatMessage)
    window["-Results-"].update(hello)
# close window at the end of application
window.close()
