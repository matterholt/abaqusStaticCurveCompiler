"""
update code, 
1) make more DRY
2) remove abaqus access to another file
3) make more versital
4) change to json, to allow for more info
5) create a visual out put via HTML
"""
# imported created modules
import odbResults #maybe an error due to the odbAccess is Abaqus library
import dataExtract
import outPutFile
import dataVis
import printData

#import some python standard libraries
import os
import re
import time


# Setting up the working locaiton,
testDir = "" # add what ever test, not sure if need
odbFile  = os.listdir(testDir)
path = os.getcwd()
print(path)

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

def main():
    FilterFiles()
    ###!! instead of calling function and adding to the dictonary how about using function to get data
    for staticFile in filterFileList:
        #gather data for dictonary 
        # 1) get data from file name of the file will be extracted
        dataExtract.FileNameData(staticFile)
        # 2) gather data from reading the  .inp file
        ### 
        # !! need to updated the process
        ### 
        dataExtract.FileReadData(testDir, staticFile["inpName"])
        # 3) obtain displacement data
        displCurve = odbResults.uData()
        staticInfo["uCurve"] = displCurve
        # 4) obtain reaction force data
        rForceCurve = odbResults.rfData()
        staticInfo["rfCurve "] = rForceCurve
        # 5) Saving data, csv or json
        outPutFile.writeResults(staticInfo)
        outPutFile.jsonFile(staticInfo)
        # 6) Data visual
        # 7)completed josb
        print("The job is completed.. Buddy!!")

if __name__ =='__main__':
    main()