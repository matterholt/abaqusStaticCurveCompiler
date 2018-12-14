#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 20:45:10 2018

@author: matterholt


REV ONE, 
needs to be refractored

"""


#the Data
u = (0,1),(1,4),(2,9),(3,17),(4,27),(5,50)
rf= (0,5),(1,12),(2,17),(3,30),(4,45),(5,70)
####


# help create the curve, 
def curve (u,rf):
    curveList = []
    for i, j in u:
        curveList = curveList + [j]
    for i, j in rf:
        curveList = curveList + [j]
    return curveList


result = curve(u,rf)
#rfResult = force(rf)


print(result)
#print(transposed)
