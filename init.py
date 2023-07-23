# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 20:16:03 2023

@author: hnewey7
"""
import os

# Function for initialisation.
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
    
    return(events, applicationName, geometry)