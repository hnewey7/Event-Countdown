# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 23:24:23 2023

@author: hnewey7
"""

from init import init
from countdownWindow import countdownWindow

# Main function.
def main():
    
    [events, applicationName, geometry] = init()
    countdownWindow(applicationName, geometry)
        
main()