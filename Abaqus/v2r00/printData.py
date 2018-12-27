"""
exporting some data out to the screen
"""
"""
   Prints and info to call to view
"""
def PrintDict ():
    print("Dictonary's Contents")
    print(staticInfo)
def PrintStaticSummary ():
    print("\n\n" + "-"*10 + "STATIC FILE REVIEW"+ "-"*10 )
    print("Analysis file is ------------> " + staticInfo['inpName'])
    print("Load Case is ----------------> " + staticInfo['loadCase'])
    print("load applied ----------------> " + staticInfo['loadDir'])
    print("Node Number -----------------> " + staticInfo['nodeNumb'])
    print("System for analysis ---------> " + staticInfo['system'])
    print("Results file ----------------> " + staticInfo['odbName'])
def FailedFile ():
    print("\n\n" + "-"*10 + "Files did not meet Requirements"+ "-"*10)
    for fileFail in noRunList:
        print("FAILED ----> " + fileFail)
def PassFile ():
    print("\n\n" + "-"*10 + "Files did meet Requirements"+ "-"*10)
    for fileApprove in filterFileList:
        print("file passed ----> " + fileApprove)
