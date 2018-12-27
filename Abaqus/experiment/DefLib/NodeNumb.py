#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 22:57:13 2018

@author: matterholt
"""
import re
#===========================================
#Defines the Node number for which the load is applied
#!future need to change "PART-1-1.1" --> need to be corrected in *.inp file
#===========================================
def DefineNodeNum():
    node = input("Load applied Node number: ")
    #RegEx requires number in the first postion to be 1 through 6
    regexPattern = r'^[1-6]'
    confirm = re.fullmatch(regexPattern,node)  
      
    #part of the path of data NEEDED
    output = "Node PART-1-1." + node    
    
    #confirm if input is good to proceed  
    if confirm :
        print ("Load applied to " + node)
        print('CHECK: ' + output)
        return output
    else:
        print("!!ERROR-> Value between 1-6")
        DefineNodeNum()

#--> historyRegions[Node PART-1-1.] --> out out should look like
DefineNodeNum()