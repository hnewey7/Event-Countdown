# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 23:24:23 2023

@author: hnewey7
"""

import os
from countdownWindow import countdownWindow

# Initialisation function
def init():
        
    # Defining key values.
    applicationName = "Event Countdown"
    geometry = "700x150"
    
    # Getting events log path.
    folderPath = os.path.dirname(os.path.abspath(__file__))
    logPath = folderPath + "\\logs\\events.txt"
    
    # Check if file exists.
    if os.path.exists(logPath):
        
        # Read file.
        log = open(logPath,"r")
        events = log.readlines()

    else:
        
        # Create log path.
        log = open(logPath,"x")
    
    return events, applicationName, geometry
    
# Main function.
def main():

    # Main GUI function.
    countdownWindow(events, applicationName, geometry)
    
def onClose():
    
    return
     
    
# Initialising.
events, applicationName, geometry = init()

# Running main function.
main()
