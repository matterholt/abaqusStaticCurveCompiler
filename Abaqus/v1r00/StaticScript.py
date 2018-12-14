"""
11-20-2018,
V01R00
script will be ran in the directory with *.odb and *.inp
1. will filter out the file that contain data
2. 
"""
import csv
import os
import re
import time
#special Abaqus module
from odbAccess import *

testDir = "" # add what ever test, not sure if need
odbFile  = os.listdir(testDir)
path = os.getcwd()
print(path)

#  Dictionary for each analysis file -> example
#    Dictionary will be constructed through script
staticInfo = {
#    "system" : "Global",
#    "loadCase" : "mbPos",
#    "inpName" : "*.inp",
#    "loadDir" : "2",
#    "nodeNum" : "10",
#    "odbName" : "*.odb"
}

#   list of files to be ran through script
filterFileList = []
#   files that do not get compiled script
noRunList = []

"""
Filter file Function
Function that will cycle through the directory. Using Regex to see if file name is correct
also the file that did not meet the requirement will be place in a no run list for confirmation
"""
def FilterFiles():
    for file in odbFile:
        patternFile = r"([a|A]nalysis_\S+[-|_](\w+).odb)"
        matchFile = re.match(patternFile, file)
        if matchFile :
            filterFileList.append(file)
        else :
            noRunList.append(file)
FilterFiles()

"""
File Name Data
Function will use the name to get some info build part of static info dictonary 
"""
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
Function will find if the analysis was performed in local or gloabal system
"""
def SystemLoad(line):
    patternSystem = r"\*Node Output, global=N0, nset=ACTUATOR"
    matchSystem = re.match(patternSystem, line)
    if matchSystem:
        staticInfo["system"] = "LOCAL"

"""
Funciton will step through inp file exicuting the function to find Load and System
"""
def FileReadData():
    inpFile = testDir + staticInfo["inpName"]
    fileLine = open(inpFile,"r")
    for line in fileLine:
        NodeLoad(line)
        SystemLoad(line)
    fileLine.close()

"""
working with the abaqus module
"""
def dispRFCurve ():
    odbFileName = staticInfo["odbName"]
    odb = openOdb(odbFileName)
    node = staticInfo["nodeNum"]
    load = staticInfo["loadDir"]
    resultPath = odb.step['Step-1'].historyRegions['Node PART-1-1.' + node ]

    """
    code needs to improved, (need to be DRY)
    function will extract the displacement and force and will 
    return the disp/rf curve to check if passed requirement
    """

    def uData():
        displacement = []
        if 'GLOBAL' in staticInfo.values():
            uDataPath = resultPath.historyOutputs['U' + load].data
        else:
            uDataPath = resultPath.historyOutputs['U' + load + 'LOCAL'].data
        # The data is time/displacement, this will remove the time 
        for disp in uDataPath:
            displacement.append(disp[1])
        return displacement
    
    def rfData():
        reactionForce = []
        if 'GLOBAL' in staticInfo.values():
            rfDataPath = resultPath.historyOutputs['RF' + load].data
        else:
            rfDataPath = resultPath.historyOutputs['RF' + load + 'LOCAL'].data
        # The data is time/displacement, this will remove the time 
        for ReactForce in rfDataPath:
            reactionForce.append(ReactForce[1])
        return reactionForce
    
    #
    displacement = uData()
    reactionForce = rfData()

    curve = zip(displacement,reactionForce)
    return curve
"""
   Prints and info to call to view
"""
def PrintDict ():
    print("Dictonary's Contents")
    print(staticInfo)
def PrintStaticSummary ():
    print("\n\n" + "-"*10 + "STATIC FILE REVIEW"+ "-"*10 )
    print("Analysis file is ------------> " + staticInfo['inpName'])
    print("Load Case is ----------------> " + staticInfo['loadCase'])
    print("load applied ----------------> " + staticInfo['loadDir'])
    print("Node Number -----------------> " + staticInfo['nodeNumb'])
    print("System for analysis ---------> " + staticInfo['system'])
    print("Results file ----------------> " + staticInfo['odbName'])
def FailedFile ():
    print("\n\n" + "-"*10 + "Files did not meet Requirements"+ "-"*10)
    for fileFail in noRunList:
        print("FAILED ----> " + fileFail)
def PassFile ():
    print("\n\n" + "-"*10 + "Files did meet Requirements"+ "-"*10)
    for fileApprove in filterFileList:
        print("file passed ----> " + fileApprove)

        

"""
funciton will export the file to a csv and name it accordingly 
"""
def writeResults (results):
    fileSave = staticInfo["loadCase"] + ".csv"
    with open(fileSave, mode='w') as csv_file:
        fieldNames = ["disp(mm)","Rforce(N)"]
        csvWriter = csv.writer(csv_file, lineterminator = '\n')
        csvWriter.writerow(fieldNames)
        for value in results:
            csvWriter.writerow(value)


def main():
    timeWait = 1
    FailedFile ()
    for odbFile in filterFileList:
        staticInfo["system"] = "GLOBAL" #hacky improve next version
        print("Starting process ...")
        FileNameData(odbFile)
        print("Reading File ...")
        time.sleep(timeWait)
        results = dispRFCurve()
        print("Saving Data ...")
        time.sleep(timeWait)
        writeResults(results)
        print("\n\nCurve Extraction complete. all is good BUDDY!!!! \n")
        staticInfo.clear()
if __name__ =='__main__':
    main()