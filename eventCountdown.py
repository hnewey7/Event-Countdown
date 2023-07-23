# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 23:06:20 2023

@author: hnewey7
"""

import tkinter as tk
import datetime 

# Countdown GUI window.
def countdownWindow():
    
    # Function to add new event.
    def addEvent():
        
        return()
    
    # Function to edit existing events.
    def editEvent():
        
        return()
    
    # Function to delete events.
    def deleteEvent():
        
        return()
    
    # Creating window with tkinter.
    countdownWindow = tk.Tk()
    countdownWindow.title(applicationName)
    countdownWindow.geometry("700x300")
    
    # Creating title for countdown window.
    title = tk.Label(countdownWindow, text=applicationName)
    
    # Creating buttons.
    addButton = tk.Button(countdownWindow, text="Add", command=addEvent)
    editButton = tk.Button(countdownWindow, text="Edit", command=editEvent)
    deleteButton = tk.Button(countdownWindow, text="Delete", command=deleteEvent)
    
    # Formatting title.
    title.grid(row=1,column=1,columnspan=3)
    
    # Formatting add button element.
    addButton.grid(row=2,column=1)
    editButton.grid(row=2,column=2)
    deleteButton.grid(row=2,column=3)
    
    # Lifting window 
    countdownWindow.lift()
    
    # Starting main loop of GUI.
    countdownWindow.mainloop()
