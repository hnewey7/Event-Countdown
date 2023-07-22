# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:34:21 2023

@author: hnewey7
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
import datetime

# Function to display add event window.
def addWindow():
    
    # Add event function
    def addButton():
        
        # Get current date.
        currentDate = datetime.date.today()
        
        # Get date from calendar.
        date = calendar.selection_get()
        
        # If date is in the future.
        if date > currentDate:
            
            return()
        
        else:
            
            # Error message popup.
            messagebox.showerror("Previous Date", "Selected event date is in the past. Please select a date in the future.")
           
    # Set event name function.
    def setName():
        
        # Get data from entry.
        name = eventName.get()
        
        # Clear entry
        eventName.delete(0,tk.END)
        
        return()
        
    # Creating window with tkinter.
    addWindow = tk.Tk()
    addWindow.title("Add Event")
    addWindow.geometry("600x220")
    
    # Defining variables.
    eventSummary = ""
    name = ""
    addHours = tk.IntVar()
    addMins = tk.IntVar()
    
    # Creating calendar element.
    calendar = Calendar(addWindow, borderwidth=0)
    
    # Creating label element.
    eventLabel = tk.Label(addWindow, text=eventSummary)
    
    # Creating event name elements.
    eventName = tk.Entry(addWindow, width=19)
    setNameButton = tk.Button(addWindow, text="Set Name", width=8, command=setName)
    
    # Creating time entry elements.
    addHoursTime = ttk.Spinbox(addWindow, from_=0, to=23, textvariable=addHours, width=6)
    addMinsTime = ttk.Spinbox(addWindow, from_=0, to=59, textvariable=addMins, width=6)
    setTimeButton = tk.Button(addWindow, text="Set Time", width=8)
    
    # Creating add event button.
    addEvent = tk.Button(addWindow, text="Add", width=15, command=addButton)
    
    # Formatting calendar element.
    calendar.grid(row=1, column=1, rowspan=4)
    
    # Formatting event label
    eventLabel.grid(row=1, column=2, columnspan=3, sticky="s")
    
    # Formatting event name elements.
    eventName.grid(row=2, column=2, columnspan=2)
    setNameButton.grid(row=2, column=4, sticky="w")
    
    # Formatting time entry elements.
    addHoursTime.grid(row=3, column=2, sticky='ne', padx=5)
    addMinsTime.grid(row=3, column=3, sticky='nw', padx=5)
    setTimeButton.grid(row=3, column=4, sticky='nw')
    
    # Formatting add event button.
    addEvent.grid(row=4, column=2, columnspan=3, sticky='n')
    
    # Configuring rows to align vertically.
    addWindow.grid_rowconfigure(0, weight=1)
    addWindow.grid_rowconfigure(1, weight=1)
    addWindow.grid_rowconfigure(2, weight=1)
    addWindow.grid_rowconfigure(3, weight=1)
    addWindow.grid_rowconfigure(4, weight=1)
    addWindow.grid_rowconfigure(5, weight=1)
    
    # Configuring columns to align horizontally.
    addWindow.grid_columnconfigure(0, weight=1)
    addWindow.grid_columnconfigure(1, weight=1)
    addWindow.grid_columnconfigure(2, weight=1)
    addWindow.grid_columnconfigure(3, weight=1)
    addWindow.grid_columnconfigure(4, weight=1)
    addWindow.grid_columnconfigure(5, weight=1)
    
    # Lifting window 
    addWindow.lift()
    
    # Starting main loop of GUI.
    addWindow.mainloop()
