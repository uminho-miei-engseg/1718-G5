import sys
from eVotUM.Cripto import eccblind

def printUsage():
    print ("init-app.py -init or init-app.py\n")

def parseArgs():
    if(len(sys.argv) > 1):
        if(sys.argv[1]=="-init"):
            init()
        else:
            printUsage()
    else:
        pR()

def pR():
    initComponents, pRDashComponents = eccblind.initSigner()
    print pRDashComponents;



def init():
    initComponents, pRDashComponents = eccblind.initSigner()
    file = open("assinante.txt", "w")
    file.write(initComponents)
    file.write("\n")
    file.write(pRDashComponents)
    file.write("\n")
    file.close()



if __name__ == "__main__":
    parseArgs()
