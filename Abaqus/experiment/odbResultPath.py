#-*- coding: utf-8 -*-
"""

1. Define load step = LOOK -->   odb.steps[Step-1]
2. Define Nodes number = LOOK --> .historyRegions[Node PART-1-1.]
3-1. Define Reaction Force = LOOK --> .historyOutputs[RF1 LOCAL].data
3-2. Define Reaction Force = LOOK --> .historyOutputs[U1 LOCAL].data
RESULTS-->(odb.steps[Step-1].historyRegions[Node PART-1-1.1].historyOutputs[U1 LOCAL].data)

!!! for full automation use the analysis.inp file to extract all data
"""

import re
import os

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
#--> odb.steps[Step-1] --> out out should look like


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


#===========================================
#Defines the Analysis System for which direction of load 
#===========================================
def DefineSystem():
    systemDef = input('DEFAULT "LOCAL" system OK? \nEnterofr Local or g for global:  ' ).lower()
    print(systemDef)
    if systemDef == 'l' or systemDef == "":
        print('--> Load is applied in "LOCAL" ')
        return "LOCAL"
    elif systemDef == 'g':
        print('--> Load is applied in "GOBAL" ')
        return "GLOBAL"
    else:
        print("!!!" + systemDef + "invalid value")
        return DefineSystem()



#===========================================
#Defines the Node number for which the load is applied
#===========================================
def LoadDirections ():
    directions = {
    "x" : "1",
    "y" : "2",
    "z" : "3",
    "xx" : "4",
    "yy" : "5",
    "zz" : "6"
    }
    loadDir = input("Load Direction is applied: ").lower()
    if loadDir in directions.keys():
        print("--> Load applied in " + loadDir)
        return directions[loadDir]
    elif loadDir in directions.values():
        print("--> Load applied in " + loadDir)
        return loadDir
    else:
        print("!!!" + "invalid value!")
        return LoadDirections ()




step = LoadStep()
system = DefineSystem()
node = DefineNodeNum()
direction = LoadDirections ()
rfDir = "RF"+ direction + " " + system
uDir = "U"+ direction + " " + system


print("\n\n================SUMMARY================")
print("--> curve wil be checked on " + '(' + step +')')
print("--> Load is applied in " + '(' + system +')')
print("--> Load is on node" + '(' +  node +')')
print("--> Load being applied in the " + '(' +  direction +')')
print("--> Reaction Force value: " + '(' + rfDir +')')
print("--> Dispacement value: "+ '(' + uDir +')')

print("\n\n================RESULT================")
#remove quotes to get to work with abaqus scritpt,,
reactionForce = '(odb.steps['+step+'].historyRegions['+node+'].historyOutputs['+rfDir+'].data'
displacement = '(odb.steps['+step+'].historyRegions['+node+'].historyOutputs['+uDir+'].data'

print(reactionForce)
print(displacement)