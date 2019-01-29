""

import numpy as np
path = "check\\mphos_Script.csv"

# Importing data for analysis

data = np.genfromtxt(path, delimiter=',', names = True)
testing = data[0:-1]

def findTarget (target,percent):
    tolarance = 1
    aboveTarget = []
    belowTarget = []
    closeTarget = []
    valueTarget = (int(target )/100 * int(percent[0:-1])/100)

#    def Info ():
#        print("\nTarget value is {} N ".format(target))
#        print("Target percent is {}".format(percent))
#        print("Tolarance of value is +\\- {}".format(tolarance))
#        print("Target searching for {} kN".format(valueTarget))
#        print("Target top value  {} N".format(highRange))
#        print("Target lowest value is {} N".format(lowRange))
#       
#    Info ()

    def valueFound (step):
#        print("\n {} is neigh !!".format(step))
        print("Time value, {} sec".format(step['Time']))
        print("Displacement value, {} mm".format(step['Disp']))
        print("Reaction Force value, {} N ".format(step['Force']))
        print("Max PEEQ value, {}  \n".format(" TO BE FOUND..."))


    def checkForTargets(tolarance):
        highRange = valueTarget + (tolarance)
        lowRange = valueTarget - (tolarance )
        for step in data:
            value = int(step['Force']) / 100
#            print(value)
            if value >= highRange:
                aboveTarget.append(step)
#                print("value {} is below {}".format(step,highRange))
            elif value <= lowRange:
                belowTarget.append(step)
#                print("value {} is below {}".format(step,lowRange))
            else:
                closeTarget.append(step)
#                valueFound (step)

    while len(closeTarget) < 1:
        tolarance = tolarance + 1
        checkForTargets(tolarance)
    else:
        print("\nThe value closes to target at {}".format(percent))
        maxValue = np.array(closeTarget[0])
        valueFound (maxValue)

percentage = ["100%","200%","300%","400%"]
for per in percentage:
    findTarget ('22600', per,)
#print("value are above target \n{}".format(aboveTarget))
#print("value are below target \n {}".format(belowTarget))