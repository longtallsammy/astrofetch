from signs import starsigns

starsignList = starsigns.signs

invalidInfoArg = 'astrofetch: invalid query'

def processInput(infoSupplied, useUnicode, printOutput, returnDate):
    #Never more than 2 args
    if len(infoSupplied) > 2:
        exit(invalidInfoArg)

    #If -d used, MUST supply 2 args
    elif len(infoSupplied) == 1:
        if returnDate != True:
            infoSupplied = str(infoSupplied)
            formattedInfo = infoSupplied.lower().title()
        else:
            exit(invalidInfoArg)

        convertStarsignToDate(formattedInfo, useUnicode)

    #Assume date is being queried and format it
    elif len(infoSupplied) == 2:
        for info in infoSupplied:
            if info.isnumeric():
                formattedDay = info
            else:
                info = info[:3]
                formattedMonth = info.lower().title()

        #Bail if user didn't supply a valid date
        try:
            if returnDate:
                return formattedMonth, formattedDay
            else:
                convertDateToStarsign(formattedMonth, formattedDay, printOutput, useUnicode)
        except:
                exit(invalidInfoArg)

def convertDateToStarsign(month, day, printOutput, useUnicode):
    monthSupplied = month[:3]
    daySupplied = day
    day30 = ['Feb', 'Apr', 'Jun', 'Sep', 'Nov']
    searchSuccess = False

    if int(daySupplied) > 31:
        exit(invalidInfoArg)
    elif int(daySupplied) > 30 and monthSupplied in day30 or int(daySupplied) > 29 and monthSupplied == day30[0]:
        exit(invalidInfoArg)

    for sign in starsignList:
        if monthSupplied == sign.startmonth[:3]:
            if daySupplied > sign.startday or daySupplied == sign.startday:
                searchSuccess = True
                foundSign = sign
                break

    if not searchSuccess:
        for sign in starsignList:
            if monthSupplied == sign.endmonth[:3]:
                searchSuccess = True
                foundSign = sign
                break

    if not searchSuccess:
        exit(invalidInfoArg)

    if printOutput:
        if not useUnicode:
            print(foundSign)
        elif useUnicode:
            print(foundSign.emoji)
    else:
        return foundSign

def convertStarsignToDate(infoSupplied, useUnicode):
    infoSupplied = str(infoSupplied[:-2][2:]).lower().title()
    searchSuccess = False

    for sign in starsignList:
        if infoSupplied == sign.name:
            searchSuccess = True
            resultForUnicode = [
                sign.emoji,
                ' ',
                sign.startmonth[:3],
                ' ',
                sign.startday,
                ' -> ',
                sign.endmonth[:3],
                ' ',
                sign.endday]
            resultForText = [
                str(sign),
                'Planet: ' + sign.planet.title(),
                'Element: ' + sign.element.title(),
                'Modality: ' + sign.modality.title()]
            break

    if not searchSuccess:
        exit(invalidInfoArg)

    if not useUnicode:
        print('\n'.join(resultForText))
    elif useUnicode:
        print(''.join(resultForUnicode))
