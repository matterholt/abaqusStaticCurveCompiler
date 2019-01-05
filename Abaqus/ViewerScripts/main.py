"""
Abaqus Viewer Script to help record Displacemenet / Reaction force Data

Abaqus Python  == 2.7

Script Detail
    1) Open Abaqus Viewer
    2) File -> Run Script
        - Suggestion: make script folder in C:\ Temp (Abaqus Default workng folder)
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

