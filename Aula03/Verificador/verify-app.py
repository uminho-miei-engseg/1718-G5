import sys
from eVotUM.Cripto import utils
from eVotUM.Cripto import eccblind

def printUsage():
    print ("verify-app.py -cert <certificado do assinante> -msg <mensagem original a assinar> -sDash <Signature> -f <ficheiro do requerente>")

def parseArgs():
    if(len(sys.argv) < 9):
        printUsage()
    else:
        if(sys.argv[1]=="-cert" and sys.argv[3]=="-msg" and sys.argv[5]=="-sDash" and sys.argv[7]=="-f"):
            main()
        else:
            printUsage()

def showResults(errorCode, validSignature):
    if (errorCode is None):
        if (validSignature):
            print("Valid signature")
        else:
            print("Invalid signature")
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the public key")
    elif (errorCode == 2):
        print("Error: pR components are invalid")
    elif (errorCode == 3):
        print("Error: blind components are invalid")
    elif (errorCode == 4):
        print("Error: invalid signature format")

def main():
    pemPublicKey = utils.readFile(sys.argv[2])
    data = sys.argv[4]
    signature = sys.argv[6]
    requerente = sys.argv[8]
    file = open(requerente, "r")
    blindComponents = file.readline()[:-1]
    pRComponents = file.readline()[:-1]
    errorCode, validSignature = eccblind.verifySignature(pemPublicKey, signature, blindComponents, pRComponents, data)
    showResults(errorCode, validSignature)

if __name__ == "__main__":
    parseArgs()
