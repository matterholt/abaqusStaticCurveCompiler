#!/bin/python 3
# _*_ coding: utf-8 _*_
"""
compile the data for the static analysis
"""
def fileNameData (staticFile):
    pattern = r"([a|A]nalysis_\S+[-|_](\w+).odb)" #it is repeat-NG
    match = re.match(pattern, staticFile )
    if match:
        staticInfo["odbName"] : staticFile
        staticInfo["inpName"] : match.group(1)
        staticInfo["loadCase"] : match.group(2)


def NodeLoad (line):
    stringPattern = r"\*MONITOR,DOF=(\d+),NODE=(\d+)"
    matchLoad = re.match(stringPattern, line)
    if matchLoad:
        staticInfo["loadDir"] = matchload.group(1)
        staticInfo["nodeNumb"] = matchload.group(2)

def systemLoad(line):
    systemPattern = r"\*Node Output, global=NO, nset=ACTUATOR"
    matchSys = re.match(systemPattern, line)
    if matchSys:
        staticInfo["system"] = "LOCAL"

def fileReadData ():
    inpFile = saveDir + staticInfo["inpName"]
    fileLine = open(inpFile,"r")
    #Context Managers: while
    #reading line by line may not be the quick way
    for line in fileLine:
        NodeLoad(line)
        systemLoad(line)
    fileline.close()
