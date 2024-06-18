from signs import signlogos

def fullsize(leftSideInfo, rightSideInfo):
    logoDict = signlogos.signs
    seasonLogo = logoDict.get(leftSideInfo.name)
    color = leftSideInfo.color

    #Spacer above output
    print('')

    #Put logo/info together line-by-line
    while rightSideInfo:
        for line in seasonLogo:
            for line in rightSideInfo:
                print(color + seasonLogo[0] + '\033[0m' + rightSideInfo[0])
                rightSideInfo.pop(0)
                seasonLogo.pop(0)

    #Print any extra lines in logo
    if seasonLogo:
        for line in seasonLogo:
            if line != '                                    ':
                print(color + line)

    #Spacer below output
    print('')

def singleLine(rightSideInfo):
    print(rightSideInfo)
