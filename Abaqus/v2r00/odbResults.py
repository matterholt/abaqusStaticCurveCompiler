##------------------------------------------
# Library from Abaqus to access results
from odbAccess *
##--------------------------------------------
def dataPath (staticInfo):
    odbFileName = staticInfo["odbName"]
    odb = openOdb(odbFileName)
    node = staticInfo['nodeNum']
    resultPath = odb.step['Step-1'].historyRegions['Node PART-1-1.' + node ]
    return resultPath

#may not need the load function
def loadDir(staticInfo):
    load = staticInfo['loadDir']
    return load

def uData(staticInfo):
    load = loadDir(staticInfo)
    resultsPath = dataPath(staticInfo)
    if 'GLOBAL' in staticInfo.values():
        uDataPathGlobalData = resultPath.historyOutputs['U' + load].data
        return uDataPathGlobalData
    else :
        uDataPathLocalData = resultPath.historyOutputs['U' + load + 'LOCAL'].data
        return uDataPathLocalData

def rfData(staticInfo):
        load = loadDir(staticInfo)
    resultsPath = dataPath(staticInfo)
    if 'GLOBAL' in staticInfo.values():
        rfDataPathGlobalData = resultPath.historyOutputs['RF' + load].data
        return rfDataPathGlobalData
    else :
        rfDataPathLocalData = resultPath.historyOutputs['RF' + load + 'LOCAL'].data
        return rfDataPathLocalData