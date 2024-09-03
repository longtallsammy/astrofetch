from signs import signlogos

def printInfo(rightSideInfo, seasonLogo, color):
    for line in seasonLogo:
        for line in rightSideInfo:
            print(color + seasonLogo[0] + '\033[0m' + rightSideInfo[0])
            rightSideInfo.pop(0)
            seasonLogo.pop(0)

def printExtraLines(seasonLogo, color):
    for line in seasonLogo:
        if line != '                                    ':
            print(color + line)

def fullsize(leftSideInfo, rightSideInfo):
    logoDict = signlogos.signs
    seasonLogo = logoDict.get(leftSideInfo.name)
    color = leftSideInfo.color

    #Spacer
    print('')

    while rightSideInfo:
        printInfo(rightSideInfo, seasonLogo, color)
        
    if seasonLogo:
        printExtraLines(seasonLogo, color)
        
    #Spacer
    print('')

def singleLine(rightSideInfo):
    print(rightSideInfo)
