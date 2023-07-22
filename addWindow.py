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
    addWindow.geometry("500x220")
    
    # Defining variables.
    addHours = tk.IntVar()
    addMins = tk.IntVar()
    
    # Creating calendar element.
    calendar = Calendar(addWindow, borderwidth=0)
    
    # Creating time entry elements.
    addHoursTime = ttk.Spinbox(addWindow, from_=0, to=23, textvariable=addHours, width=6)
    addMinsTime = ttk.Spinbox(addWindow, from_=0, to=59, textvariable=addMins, width=6)
    
    # Creating add event button.
    addEvent = tk.Button(addWindow, text="Add", width=15)
    
    # Formatting calendar element.
    calendar.grid(row=1, column=1, rowspan=2)
    
    # Formatting time entry elements.
    addHoursTime.grid(row=1, column=2, sticky="se", pady=8, padx=5)
    addMinsTime.grid(row=1, column=3, sticky="sw", pady=8)
    
    # Formatting add event button.
    addEvent.grid(row=2, column=2, columnspan=2, sticky="n")
    
    # Configuring rows to align vertically.
    addWindow.grid_rowconfigure(0, weight=1)
    addWindow.grid_rowconfigure(1, weight=1)
    addWindow.grid_rowconfigure(2, weight=1)
    addWindow.grid_rowconfigure(3, weight=1)
    
    # Configuring columns to align horizontally.
    addWindow.grid_columnconfigure(0, weight=1)
    addWindow.grid_columnconfigure(1, weight=1)
    addWindow.grid_columnconfigure(2, weight=1)
    addWindow.grid_columnconfigure(3, weight=1)
    addWindow.grid_columnconfigure(4, weight=1)
    
    # Lifting window 
    addWindow.lift()
    
    # Starting main loop of GUI.
    addWindow.mainloop()
