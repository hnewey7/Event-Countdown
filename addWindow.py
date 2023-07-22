# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:34:21 2023

@author: hnewey7
"""

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

# Function to display add event window.
def addWindow():
    
    # Creating window with tkinter.
    addWindow = tk.Tk()
    addWindow.title("Add Event")
    addWindow.geometry("500x300")
    
    # Defining variables.
    addHours = tk.IntVar()
    addMins = tk.IntVar()
    
    # Creating calendar element.
    calendar = Calendar(addWindow, borderwidth=0)
    
    # Creating time entry elements.
    addHoursTime = ttk.Spinbox(addWindow, from_=0, to=23, textvariable=addHours, width=6)
    addMinsTime = ttk.Spinbox(addWindow, from_=0, to=59, textvariable=addMins, width=6)
    
    # Creating add event button.
    addEvent = tk.Button(addWindow, text="Add")
    
    # Formatting calendar element.
    calendar.grid(row=1, column=1, rowspan=2)
    
    # Formatting time entry elements.
    addHoursTime.grid(row=1, column=2, sticky="s")
    addMinsTime.grid(row=1, column=3, sticky="s")
    
    # Formatting add event button.
    addEvent.grid(row=2, column=2, columnspan=2, sticky="n")
    
    # Lifting window 
    addWindow.lift()
    
    # Starting main loop of GUI.
    addWindow.mainloop()
