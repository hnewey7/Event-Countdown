# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:34:21 2023

@author: hnewey7
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
import pandas
import datetime
import os

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
        
        # Defining global variables.
        global name
        global eventDatetime
        
        # Check if all information has been inputted.
        if len(name)==0 or eventDatetime==None:
            messagebox.showerror("Invalid Event Information", "Please enter all valid event information.")
        
        else:
            # Get folder path.
            folderPath = os.path.dirname(os.path.abspath(__file__))
            
            # Log file path.
            logPath = folderPath + "\\logs\\events.txt"
            
            # Opening .txt file.
            log = open(logPath,"x")
            
            # Writing event to file.
            log.write(f'{name} - {eventDatetime}\n')
            
            # Closing log file
            log.close()
            
            # Closing the add window.
            addWindow.destroy()    
        
        return()
    
    # Set event name function.
    def setName():
        
        # Defining global variables.
        global name
        
        # Get data from entry.
        name = eventName.get()
        
        # Clear entry
        eventName.delete(0,tk.END)
        
        # Update event summary.
        updateEventSum()
        
    # Set event time function.
    def setTime():
        
        # Defining global variables.
        global eventDatetime
        
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
        
        # Update event summary
        updateEventSum()
    
    # Function to update event summary.
    def updateEventSum():
        
        # Defining global variables.
        global name
        global eventDatetime
        
        # Getting current datetime.
        currentTime = datetime.datetime.now()
        
        # Formatting depending on the data available.
        if len(name)==0 and eventDatetime==None:
            eventSummary = ''
            
        elif len(name)!=0 and eventDatetime==None:
            eventSummary = f'{name}'
        
        elif len(name)==0 and eventDatetime!=None:
            raw_timer = eventDatetime - currentTime
            timer = pandas.to_timedelta(raw_timer).round('1s')
            eventSummary = f'{timer}'
            
        else:
            raw_timer = eventDatetime - currentTime
            timer = pandas.to_timedelta(raw_timer).round('1s')
            eventSummary = f'{name}: {timer}'
        
        # Configuring the label.
        eventLabel.config(text=eventSummary)
        
        # Repeating every second.
        addWindow.after(1000,updateEventSum)
        
    # Creating window with tkinter.
    addWindow = tk.Tk()
    addWindow.title("Add Event")
    addWindow.geometry("600x220")
    
    # Defining variables.
    global name
    name = ""
    global eventDatetime
    eventDatetime = None
    addHours = tk.IntVar()
    addMins = tk.IntVar()
    
    # Creating calendar element.
    calendar = Calendar(addWindow, borderwidth=0)
    
    # Creating label element.
    eventLabel = tk.Label(addWindow, text="")
    
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
    
    # Running update event summary.
    updateEventSum()
    
    # Lifting window 
    addWindow.lift()
    
    # Starting main loop of GUI.
    addWindow.mainloop()
