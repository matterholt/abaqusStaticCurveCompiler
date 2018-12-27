#-*- coding: utf-8 -*-


import re
import os

print(os.getcwd())

#/Users/matterholt/Projects/Python/Abaqus/work/testFiles

filteredInp = []
testDir = "/testFiles"
test = os.chdir(testDir)
print(test)

inpFile = os.listdir(testDir)

for file in inpFile:
    inpPattern = r"[a|A]nalysis_\S+[-|_](\w).inp"
    match = re.fullmatch(inpPattern, file)
    if match:
        # inp file --> need to read throught find more data
        filteredInp.append(file)
        # ladCase, use a filename
        loadCase = match.group(1)
        filteredInp.append(loadCase)
        #odb file to perform the extraction
        odbFile = file[0:-4] + ".odb"
        filteredInp.append(odbFile)

print(filteredInp)