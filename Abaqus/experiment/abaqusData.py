#!/bin/python 3
# _*_ coding: utf-8 _*_
"""

"""
import odbAccess import*

def dispRFCurve ():
    odbFileName = staticInfo["odbName"]
    odb = openOdb (odbFileName)
    node = staticInfo["nodeNum"]
    load = staticInfo["loadDir"]
    resultPath = odb.steps['Step-1'].historyRegions['Node Part-1-1.' + node]

##==================================================
## this need to be refractored, do not like how the code is repeated
## the only diferance is is displacement and reactionforce
##==================================================
    def uData():
        displacement = []
        if 'GLOBAL' in staticInfo.values():
            uDataPath = resultPath.historyOutputs['U' + load].data
            return uDataPath
        else:
            uDataPath = resultPath.historyOutputs['U' + 'local'].data
            return uDataPath
#! Does this need to be in code, check
#        for disp in uDataPath:
#            displacement.append(disp[1])
#        return displacement

    def rfData():
        reactionForce = []
        if 'GLOBAL' in staticInfo.values():
            rfDataPath = resultPath.historyOutputs['RF' + load].data
            return rfDataPath
        else:
            rfDataPath = resultPath.historyOutputs['RF' + 'local'].data
            return rfDataPath
        
    #add  Values to
    displacement = uData()
    reactionForce = rfData()

    curve = zip(displacement,reactionForce)
    return curve

##+++++++++++++++++++++++++++++++++++++++++++
#   write data to the excel
#      need to be reviewed
##++++++++++++++++++++++++++++++++++++++++++
def writeResults(results):
    #file name is define by the load case define by dict, 
    ### need to change or something better
    fileSave = StaticInfo["loadCase"] + ".csv"
    with open(fileSave, mode='w') as resultFile
    fieldNames = ['Displacement','ReactionForce']
    csvwriter = csv.writer(resultFile, lineterminator = '\n')
    csvwriter.writerow(fieldNames)
    for line in results:
        csvwriter.writerow(line)