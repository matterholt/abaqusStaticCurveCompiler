"""
Abaqus Viewer Script to help record Displacemenet / Reaction force Data

Abaqus Python  == 2.7

Script Detail
    1) Open Abaqus Viewer
    2) File -> Run Script
        - Suggestion: make script folder in C:\\ Temp (Abaqus Default workng folder)
    3) Scipt loaded succesful noted in the Abaqus "message area".
    4) Below "message area" should be " >>> " = Abaqus Kernal and where function exicuted

Function available
    1) Get_curve() will gather data for Disp / Force Curve and save a .csv file
"""
# Abaqus Modules
#from odbAccess import *
#from abaqus immport import session
# Python Standard Libraries
import csv
import os

def ConfirmResultDir ():
    """ Check if folder is created for result .csv"""
    #TODO make paths for folder compatiable with other OS
    path = os.path.join("00__Results")
    checkFolder = os.path.isdir("path")
    absPath = os.path.abspath(path)
    if checkFolder == False:
        os.mkdir(".\\00__Results")
        print("Folder created. \n {} ".format(absPath))

def CurveCompile ( disp, force):
    """Takes raw data, refinds it for a curve"""
    time = []
    dispVal = []
    forceVal = []
    for time in disp:
        time.append(time[0])
    for u in disp:
        dispVal.append(u[1])
    for f in force:
        forceVal.append(f[1])
    curve = zip(time, dispVal, forceVal)
    return curve

def WriteResults (name, results):
    """outputs a .csv file that has analysis curve to the current directory """
    #TODO !!! for the filSaved, test if can place all in results folder
    fileSaved = "{}.csv".format(name)
    with open(fileSaved, mode="w") as csvFile:
        fieldNames = ['Time','Disp.','Force']
        csvWriter = csv.writer(csvFile, lineterminator = "\n")
        csvWriter.writerow(fieldNames)
        for data in results:
            csvWriter.writerow(data)

def MainDataPath (odb,nodeLoad):
    """ Comon path for displacement and force"""
    dataResults = odb.steps.values()[-1].historyRegions['Node Part-1-1'+ nodeLoad]
    return dataResults

def TimeDisp (odb,nodeLoad,direction):
    """
    Gathers data on a specific node number. Data is in odb data base, 
    specificaly for time / Displacment
    """
    path = MainDataPath(odb,nodeLoad)
    timeDispData = path.historyOutputs['U' + direction].data
    return timeDispData

def TimeForce (odb,nodeLoad,direction):
    """
    Gathers data on a specific node number. Data is in odb data base, 
    specificaly for time / Reaction Force
    """
    path = MainDataPath(odb,nodeLoad)
    timeForceData = path.historyOutputs['RF' + direction].data
    return timeForceData

def Get_curve():
    """
    This is the main function of script.
    Script was to be run with what ever odb result are displayed in the abaqus viewport.
    and is able to be ran multiple time in one session. (no need to file->Run Script everytime)
    """
    print ("\n-----  Executing Script  -----\n ")
    ConfirmResultDir()
    fields = (("Analysis Name: ",""), ("Node Number: ",""),("Load Dir (1,2,3)",""))
    #getInputs is Abaqus specific 
    fileName, nodeNumber, loadDir = getInputs( fields = fields, Label = "Analysis Name: ","Node Number: ","Load Dir (1,2,3)" )
    vp = session.viewport[session.currentViewportName]
    odb = vp.displayedObject
    ####### TODO check on code above
    timeDispCurve = TimeDisp(odb,nodeNumber,nodeLoad)
    timeForceCurve = TimeForce(odb,nodeNumber,nodeLoad)
    timeDispForceCurve = CurveCompile(timeDispCurve,timeForceCurve)
    WriteResults(fileName,timeDispForceCurve )
    path = os.getcwd()
    resultLocation = os.path.abspath(path)
    print("\n-----  Curve has been save \n {}  -----\n ".format(resultLocation))


