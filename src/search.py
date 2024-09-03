from signs import starsigns

starsignList = starsigns.signs

invalidInfoArg = 'astrofetch: invalid query'

def attemptSignConversion(returnDate, infoSupplied, invalidInfoArg, useUnicode):
    if returnDate != True:
        infoSupplied = str(infoSupplied)
        formattedInfo = infoSupplied.lower().title()
    else:
        exit(invalidInfoArg)

    convertStarsignToDate(formattedInfo, useUnicode)

def attemptDateConversion(infoSupplied, returnDate, printOutput, useUnicode):
    for info in infoSupplied:
        if info.isnumeric():
            formattedDay = info
        else:
            info = info[:3]
            formattedMonth = info.lower().title()

    try:
        return formattedMonth, formattedDay
    except:
        exit(invalidInfoArg)

    
def processInput(infoSupplied, useUnicode, printOutput, returnDate):
    #Never more than 2 args
    if len(infoSupplied) > 2:
        exit(invalidInfoArg)

    elif len(infoSupplied) == 1:
        attemptSignConversion(returnDate, infoSupplied, invalidInfoArg, useUnicode)
        
    elif len(infoSupplied) == 2:
        formattedMonth, formattedDay = attemptDateConversion(infoSupplied, returnDate, printOutput, useUnicode)

        try:
            if returnDate:
                return formattedMonth, formattedDay
            else:
                convertDateToStarsign(formattedMonth, formattedDay, printOutput, useUnicode)
        except:
            exit(invalidInfoArg)
    
def identifySignFromDate(starsignList, daySupplied, monthSupplied, invalidInfoArg):
    for sign in starsignList:
        if monthSupplied == sign.startmonth[:3]:
            if daySupplied > sign.startday or daySupplied == sign.startday:
                return sign

    for sign in starsignList:
        if monthSupplied == sign.endmonth[:3]:
            return sign

    exit(invalidInfoArg)

def convertDateToStarsign(month, day, printOutput, useUnicode):
    monthSupplied = month[:3]
    daySupplied = day
    day30 = ['Feb', 'Apr', 'Jun', 'Sep', 'Nov']

    if int(daySupplied) > 31:
        exit(invalidInfoArg)
    elif int(daySupplied) > 30 and monthSupplied in day30 or int(daySupplied) > 29 and monthSupplied == day30[0]:
        exit(invalidInfoArg)

    foundSign = identifySignFromDate(starsignList, daySupplied, monthSupplied, invalidInfoArg)

    if printOutput:
        if not useUnicode:
            print(foundSign)
        elif useUnicode:
            print(foundSign.emoji)
    else:
        return foundSign

def processSignForUnicode(sign):
    resultForUnicode = [
        sign.emoji,
        sign.startmonth[:3],
        sign.startday,
        '->',
        sign.endmonth[:3],
        sign.endday
    ]

    return resultForUnicode

def processSignForText(sign):
    resultForText = [
        str(sign),
        'Planet: ' + sign.planet.title(),
        'Element: ' + sign.element.title(),
        'Modality: ' + sign.modality.title()
    ]
    return resultForText

def identifyDateFromSign(starsignList, infoSupplied):
    for sign in starsignList:
        if infoSupplied == sign.name:
            return sign
            
    exit(invalidInfoArg)

def convertStarsignToDate(infoSupplied, useUnicode):
    infoSupplied = str(infoSupplied[:-2][2:]).lower().title()

    foundSign = identifyDateFromSign(starsignList, infoSupplied)

    if not useUnicode:
        textResult = processSignForText(foundSign)
        print('\n'.join(textResult))
    elif useUnicode:
        textResult = processSignForUnicode(foundSign)
        print(' '.join(textResult))

