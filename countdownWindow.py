# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 23:06:20 2023

@author: hnewey7
"""

import tkinter as tk
import datetime
from addWindow import addWindow

# Countdown GUI window.
def countdownWindow(events, applicationName, geometry):
    
    # Function to add new event.
    def addEvent():
        
        # Function to launch add window.
        addWindow(events)
           
    # Function to edit existing events.
    def editEvent():
        
        return()
    
    # Function to delete events.
    def deleteEvent():
        
        return()
    
    def updateEvents():
        
        # Getting length of events.
        eventNumber = len(events)
        
        # Check for events.
        if eventNumber!=0:
            
            for event in events:
                
                event = tk.Label(countdownWindow)
        
        # Creating title for countdown window.
        title = tk.Label(countdownWindow, text=applicationName, pady=5)
        
        # Creating buttons.
        addButton = tk.Button(countdownWindow, text="Add", command=addEvent, width=15)
        editButton = tk.Button(countdownWindow, text="Edit", command=editEvent, width=15)
        deleteButton = tk.Button(countdownWindow, text="Delete", command=deleteEvent, width=15)
        
        # Formatting title.
        title.grid(row=1,column=1,columnspan=3)
        
        # Formatting add button element.
        addButton.grid(row=eventNumber+2,column=1)
        editButton.grid(row=eventNumber+2,column=2)
        deleteButton.grid(row=eventNumber+2,column=3)
        
        # Configuring rows to align vertically.
        for i in range(eventNumber+4):
            countdownWindow.grid_rowconfigure(i, weight=1)
        
        # Configuring columns to align horizontally.
        countdownWindow.grid_columnconfigure(0, weight=1)
        countdownWindow.grid_columnconfigure(1, weight=1)
        countdownWindow.grid_columnconfigure(2, weight=1)
        countdownWindow.grid_columnconfigure(3, weight=1)
        countdownWindow.grid_columnconfigure(4, weight=1)
        
        # Repeat every second.
        countdownWindow.after(1000, updateEvents)
    
    # Creating window with tkinter.
    countdownWindow = tk.Tk()
    countdownWindow.title(applicationName)
    countdownWindow.geometry(geometry)
    
    # Update events function.
    updateEvents()
    
    # Lifting window 
    countdownWindow.lift()
    
    # Starting main loop of GUI.
    countdownWindow.mainloop()
