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
    
    # Function to format the spin box.
    def formatSpin(spinboxName):
        
        # Get value from spinbox.
        value = spinboxName.get()
        
        # Format the value.
        formattedValue = "{:02d}".format(int(value))
        
        # Setting to formatted value.
        spinboxName.set(formattedValue)
        
        # Setting icursor.
        spinboxName.icursor(tk.END)
        
        # Setting selection.
        spinboxName.select_range(0, tk.END)
            
    # Add event function
    def addButton():
           
        return()
    
    # Set event name function.
    def setName():
        
        # Get data from entry.
        data = eventName.get()
        
        # Clear entry
        eventName.delete(0,tk.END)
        
    # Set event time function.
    def setTime():
        
        try:
            # Getting time data.
            hours = int(addHoursTime.get())
            mins = int(addMinsTime.get())
        except:
            # Error message popup.
            messagebox.showerror("No Time Input", "Please input a valid time.")
        
        date = str(calendar.selection_get())
        
        # Splitting date into componenets
        dateComponents = date.split("-")
        
        # Individual components
        year = int(dateComponents[0])
        month = int(dateComponents[1])
        day = int(dateComponents[2])
        
        # Converting to datetime.
        Datetime = datetime.datetime(year, month, day, hours, mins)
        
        # Get current date.
        currentDate = datetime.datetime.now()
        
        # If date is in the future.
        if Datetime > currentDate:
            
            # Setting event datimetime.
            eventDatetime = Datetime
        
        else:
            
            # Error message popup.
            messagebox.showerror("Previous Date", "Selected event date is in the past. Please select a date in the future.")
            
        # Clearing input box.
        addHoursTime.set("")
        addMinsTime.set("")
    
    # Creating window with tkinter.
    addWindow = tk.Tk()
    addWindow.title("Add Event")
    addWindow.geometry("600x220")
    
    # Defining variables.
    name = ""
    eventDatetime = ""
    eventSummary = ""
    addHours = tk.IntVar()
    addMins = tk.IntVar()
    
    # Creating calendar element.
    calendar = Calendar(addWindow, borderwidth=0)
    
    # Creating label element.
    eventLabel = tk.Label(addWindow, text=eventSummary)
    
    # Creating event name elements.
    eventName = tk.Entry(addWindow, width=19, justify="center")
    setNameButton = tk.Button(addWindow, text="Set Name", width=8, command=setName)
    
    # Creating time entry elements.
    addHoursTime = ttk.Spinbox(addWindow, from_=0, to=23, textvariable=addHours, width=6, justify="center", command=lambda: formatSpin(addHoursTime))
    addMinsTime = ttk.Spinbox(addWindow, from_=0, to=59, textvariable=addMins, width=6, justify="center", command=lambda: formatSpin(addMinsTime))
    setTimeButton = tk.Button(addWindow, text="Set Time", width=8, command=setTime)
    
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
