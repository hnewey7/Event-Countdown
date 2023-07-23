# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 23:24:23 2023

@author: hnewey7
"""

from init import init
from countdownWindow import countdownWindow

# Defining key values.
applicationName = "Event Countdown"
geometry = "700x150"

# Main function.
def main():
    
    init()
    countdownWindow(applicationName, geometry)
        
main()