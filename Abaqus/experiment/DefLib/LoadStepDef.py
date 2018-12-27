#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 22:46:32 2018

@author: matterholt
"""
'''
function used to ask user what step to run the script on

--> step one to create the Displacement/ReactionForce curve
'''

#===========================================
#Defines the load step for displacement / ReactionForce
#===========================================
def LoadStep():
    defaultStep = input('Default "Step-1" OK% \nhit Enter to confirm or "n" To change Step number: ')
    if defaultStep == "n":
        newStepNum = input("Enter Step number: ")
        loadStepResult = "Step-"+newStepNum
        print("--> Step is applied in " + loadStepResult)
        return loadStepResult
 
    elif defaultStep == "" or defaultStep =='y':
        loadStep = "Step-1"
        print("--> Step is applied in " + loadStep)
        return loadStep

    else:
        print("!!! --> "+ defaultStep + "is invalid")
        return LoadStep()

LoadStep()