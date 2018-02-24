import sys
from eVotUM.Cripto import utils
from eVotUM.Cripto import eccblind

def printUsage():
    print ("desofusca-app.py -s <Blind Signature> -RDash <pRDashComponents>")

def parseArgs():
    if(len(sys.argv) < 3):
        printUsage()
    else:
        if(sys.argv[1]=="-s" and sys.argv[3]=="-RDash"):
            main()
        else:
            printUsage()

def showResults(errorCode, signature):
    if (errorCode is None):
        print("Signature: %s" % signature)
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")
    elif (errorCode == 2):
        print("Error: blind components are invalid")
    elif (errorCode == 3):
        print("Error: invalid blind signature format")

def main():
    blindSignature = sys.argv[2]
    pRDashComponents = sys.argv[4]
    file = open("requerente.txt", "r")
    blindComponents = file.readline()[:-1]
    errorCode, signature = eccblind.unblindSignature(blindSignature, pRDashComponents, blindComponents)
    showResults(errorCode, signature)

if __name__ == "__main__":
    parseArgs()
