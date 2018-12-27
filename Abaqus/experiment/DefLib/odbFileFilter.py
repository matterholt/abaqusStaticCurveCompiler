#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 21:36:08 2018

@author: matterholt

!!! make this the main, then call the function from other files
!!! need to make a loop for the clean list that will run list through program

"""
'''
OPTION 1: 
    prompts user for where the odb result file are at
path = input('results file location')
dirs = os.listdir(path)

OPTION 2:
    place python file in folder and will find all odb files in folder
    
OPTION 3:
    Hard code path 
'''

import re
import os, sys

#--to check --
testlist = [
        'analysis_T3C_FrSub_V30r00-FtPOS.odb',
        'Analysis_tsx_FrSub_v34r02_FhPOS.odb',
        'analysis_4GS_FrSub_V62r20-MBNeg.odb',
        'Analysis_I0S_FrSub_V11r625-MTpos.odb',
        'Analysis_I0S_FrSub_V11r625-MTpos.inp',
        'Analysis_I0S_FrSub_V11r625-MTpos.msg',
        'Analysis_I0S_FrSub_V11r625-MTpos.dat',
        'Analysis_I0S_FrSub_V11r625-ftpos.odb_f',
        'Analysis_2SU_FrSub_V00r00-mbneg.odb',
        'Analysis_PKND_FrSub_V52r83_fhpos.odb',
        'Analysis_5NIV_FrSub_V30r05a_MBNEG.odb']

'''
#path is  desired out come
#path = "openOdb('analysis_camGuide_v09r00-v35r09b.odb')"


filePath = "--test--> C:\\testpython\\results\\"
dirs = os.listdir(filePath)
'''

# List of files in folder
fileList = []
# List of files that will be ran through the program
cleanList = []
# files that do not meet requirement
errorList = []

# loop through folder and append to list
def GetFiles(dirs):
    for file in dirs:
        fileList.append(file)
    
#remove files the do not meet the the regex of .odb
def CleanFiles(fileList):
    for file in fileList:
        #RegEx pattern requires char with non-white space .odb
        pattern = r"(\w+\S+.odb)"
        match = re.fullmatch(pattern, file)
        #check if file meet requirement to run program
        if match:
            cleanList.append(file)
        else:
            errorList.append(file)

CleanFiles(testlist)
print('\nFiles did not meet requirement')
print(errorList)
print('\nFiles that will be processed')
print(cleanList)

#future work to get the openOdb() path to extract data
officalList = ['analysis_T3C_FrSub_V30r00-FtPOS.odb',
               'Analysis_tsx_FrSub_v34r02_FhPOS.odb', 
               'analysis_4GS_FrSub_V62r20-MBNeg.odb',
               'Analysis_I0S_FrSub_V11r625-MTpos.odb', 
               'Analysis_2SU_FrSub_V00r00-mbneg.odb', 
               'Analysis_PKND_FrSub_V52r83_fhpos.odb', 
               'Analysis_5NIV_FrSub_V30r05a_MBNEG.odb']