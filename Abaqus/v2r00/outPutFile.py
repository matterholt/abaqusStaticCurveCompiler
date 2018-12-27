"""
working with some data vis libraries
"""
import csv



# Saving the data
# 1-1, saveing a csvfile
"""
funciton will export the file to a csv and name it accordingly 
"""
def writeResults (results):
    fileSave = title + ".csv"
    with open(fileSave, mode='w') as csv_file:
        fieldNames = ["disp(mm)","Rforce(N)"]
        csvWriter = csv.writer(csv_file, lineterminator = '\n')
        csvWriter.writerow(fieldNames)
        for value in results:
            csvWriter.writerow(value)

def jsonFile(StaticInfo):
    fileSave = StaticInfo["loadCase"] + ".json"
    with open (fileSave, "w") as writeFile:
        json.dump(StaticInfo, writeFile)
