#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 21:56:06 2018

@author: matterholt
"""
import csv
import os 
import time
import re
#from odbAccess import *
def main():
    path = os.getcwd()
#    path = "/Users/matterholt/Projects/Python/Abaqus/work/v1r00"
    odbFile = os.listdir(path)
    
    sec = 2 #keep file from loading too fast
    
    #Dictionary for each analysis file
    staticInfo = {
#            "loadCase"  : "FtNeg",
#            "inpName"   : "*.inp",
#            "loadDir"   : "2", #x=1, y=2, z=3
#            "nodeNumb"  : "10",
#            "system"    : "LOCAL",
#            "odbName"   : "*.odb"
            }
    filteredFile = []
    noRunList = []
    
# =============================================================================
#     Filtered directories
# =============================================================================
    def filterFiles():
        for file in odbFile:
            odbPattern = r"[a|A]nalysis.*\.odb"
            match = re.match(odbPattern, file)
            if match:
                filteredFile.append(file)
            else:
                noRunList.append(file)
# =============================================================================
#     Data Extraction Process on file name
# =============================================================================
    def fileNameData(staticFile):
        odbPattern = r"([a|A]nalysis_\S+[-|_](\w+)).odb"
        matchOdb = re.match(odbPattern,staticFile)
        if matchOdb:
            staticInfo["odbName"] = (staticFile)
            staticInfo["inpName"] = (matchOdb.group(1)+ '.inp')
            staticInfo["loadCase"] = (matchOdb.group(2))
            
# =============================================================================
#  extracting data file 
# =============================================================================
    def nodeLoad(line):
        nodePattern = r"\*MONITOR,DOF=(\d+),NODE=(\d+)"
        matchLoad = re.match(nodePattern, line)
        if matchLoad:
            staticInfo["loadDir"] = (matchLoad.group(1))
            staticInfo["nodeNumb"] = (matchLoad.group(2))
        
# =============================================================================
#   Read file and closing
# =============================================================================
    def fileReadData():
        inpFile = path + staticInfo["inpName"]
        fileLine = open(inpFile,"r")
        for line in fileLine:
            nodeLoad(line)
        fileLine.close()
# =============================================================================
#   Prints and info to call to view
# =============================================================================
    def printDict ():
        print("Dictonary's Contents")
        print(staticInfo)
    def printStaticSummary ():
        print("\n\n" + "-"*10 + "STATIC FILE REVIEW"+ "-"*10 )
        print("Analysis file is ------------> " + staticInfo['inpName'])
        print("Load Case is ----------------> " + staticInfo['loadCase'])
        print("load applied ----------------> " + staticInfo['loadDir'])
        print("Node Number -----------------> " + staticInfo['nodeNumb'])
        print("System for analysis ---------> " + staticInfo['system'])
        print("Results file ----------------> " + staticInfo['odbName'])
    def failedFile ():
        print("\n\n" + "-"*10 + "Files did not meet Requirements"+ "-"*10)
        for fileFail in noRunList:
            print("FAILED ----> " + fileFail)

# =============================================================================
#     
# =============================================================================
    def staticCompiler():
        filterFiles()
        print(filteredFile)
#        printfileToExtract()
        for staticFile in filteredFile:
            fileNameData(staticFile)
            time.sleep(sec)
            
            
            printStaticSummary ()
            
    staticCompiler()
if __name__ == "__main__":
    main()
    
    