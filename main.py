# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 23:24:23 2023

@author: hnewey7
"""

import os
import tkinter as tk
#from countdownWindow import countdownWindow

# Initialisation function
def init():
        
    # Defining key values.
    applicationName = "Event Countdown"
    geometry = "700x150"
    print(f'Key values set: {applicationName} {geometry}')
    
    # Getting events log path.
    folderPath = os.path.dirname(os.path.abspath(__file__))
    logPath = folderPath + "\\logs\\events.txt"
    print(f'Folder path: {folderPath}')
    print(f'Log path: {logPath}')
    
    # Check if file exists.
    if os.path.exists(logPath):
        
        print('Log file exists.')
        # Read file.
        log = open(logPath,"r")
        events = log.readlines()
        print(f'Current events: {events}')
        

    else:
        
        print('Log file does not exits.')
        # Create log path.
        log = open(logPath,"x")
        print('Log file created.')
    
    return events, applicationName, geometry, log
    
# Main function.
def main():
    
    # Creating window with tkinter.
    mainWindow = tk.Tk()
    mainWindow.title(applicationName)
    mainWindow.geometry(geometry)
    
    # Update events function.
    #updateEvents()
    
    # Lifting window 
    mainWindow.lift()
    
    # On close function.
    mainWindow.protocol("WM_DELETE_WINDOW", lambda:onClose(mainWindow, log))
    
    # Starting main loop of GUI.
    mainWindow.mainloop()
    
    # Main GUI function.
    #countdownWindow(events, applicationName, geometry)

def onClose(mainWindow, log):
    
    # Saving log file.
    log.close()
    print('File saved.')
    
    # Closing window.
    mainWindow.destroy()
    print('Main window closed.')

# Initialising.
events, applicationName, geometry, log = init()

# Running main function.
main()
