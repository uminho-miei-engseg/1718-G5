import sys
from eVotUM.Cripto import utils
from eVotUM.Cripto import eccblind

def printUsage():
    print ("blindSignature-app.py -key <chave privada> -bmsg <Blind message>")

def parseArgs():
    if(len(sys.argv) < 3):
        printUsage()
    else:
        if(sys.argv[1]=="-key" and sys.argv[3]=="-bmsg"):
            main()
        else:
            printUsage()

def showResults(errorCode, blindSignature):
    if (errorCode is None):
        print("Blind signature: %s" % blindSignature)
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the private key")
    elif (errorCode == 2):
        print("Error: init components are invalid")
    elif (errorCode == 3):
        print("Error: invalid blind message format")

def main():
    pemKey = utils.readFile(sys.argv[2])
    blindM = sys.argv[4]
    file = open("assinante.txt", "r")
    initComponents = file.readline()[:-1]

    errorCode, result = eccblind.generateBlindSignature(pemKey, "" , blindM, initComponents)
    showResults(errorCode, result)

if __name__ == "__main__":
    parseArgs()
