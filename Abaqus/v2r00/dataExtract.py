'''
Library to create dictonary for the odb file

'''
"""
File Name Data
Function will use the name to get some info build part of static info dictonary 

!!this module needed to be updated, 
 need to be be refine to work with modules and 
"""
import re

def FileNameData(staticFile):
    patternName = r"([a|A]nalysis_\S+[-|_](\w+).odb)" #same as Filter should improve
    matchName = re.match(patternName, staticFile)
    if matchName:
        staticFile["odbName"] = staticFile
        staticFile["loadCase"] = matchName.group(2)
        staticFile["inpName"] = staticFile[0:-4] + '.inp'
"""
Node Load
Function will search through the file line by line looking for the Regex pattern
data wil create the load direction and the node number.
"""
def NodeLoad(line):
    patternString = r"\*MONITOR,DOF=(\d+),NODE=(\d+)"
    matchLoad = re.match(patternString, line)
    if matchLoad:
        staticInfo["loadDir"] = matchLoad.group(1)
        staticInfo["nodeNum"] = matchLoad.group(2)
    
"""
System for load
Function will find if the analysis was performed in local or global system
"""
def SystemLoad(line):
    patternSystem = r"\*Node Output, global=N0, nset=ACTUATOR"
    matchSystem = re.match(patternSystem, line)
    if matchSystem:
        staticInfo["system"] = "LOCAL"

"""
Funciton will step through inp file exicuting the function to find Load and System
"""
def FileReadData(testDir, inpName):
    inpFile = testDir + inpName
    fileLine = open(inpFile,"r")
    for line in fileLine:
        NodeLoad(line)
        SystemLoad(line)
    fileLine.close()
