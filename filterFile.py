#!/bin/python 3
# _*_ coding: utf-8 _*_
"""
module : filter through the directory looking for odb file
!! need to be a module for the main
"""
import re

def filteFiles():
    cleanFiles = []
    for file in odbFile :
        odbPattern = r"[a|A]nalysis_\S+[-|_](\w+).odb" #it is repeat-NG
        odbMatch = re.match(odbPattern,file)
        if odbMatch:
            cleanFiles.append(file)
        else:
            noRunList.append(file)
return cleanFiles
