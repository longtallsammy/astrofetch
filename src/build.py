from signs import signlogos

def fullFetch(leftSideInfo, rightSideInfo):
    logoDict = signlogos.signs
    for prettyname, logo in logoDict.items():
        if prettyname == leftSideInfo.name:
            seasonlogo = logo

    rightSide = list(rightSideInfo)
    print('')

    color = leftSideInfo.color

    rightSideInfo = list(rightSideInfo)

    while rightSideInfo:
        for line in seasonlogo:
            for line in rightSideInfo:
                print(color + seasonlogo[0] + '\033[0m' + rightSideInfo[0])
                rightSideInfo.pop(0)
                seasonlogo.pop(0)

    if seasonlogo:
        for line in seasonlogo:
            if line != '                                    ':
                print(color + line)
    print('')

def smallFetch(rightSideInfo):
    print(rightSideInfo)

def miniFetch(rightSideInfo):
    print(rightSideInfo)

