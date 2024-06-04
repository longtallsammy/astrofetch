from signs import starsigns

starsignList = starsigns.signs

errShowUsage = 'usage: astrofetch [-h] [-s] [-m] [-u] [-i  [...]]\n'
invalidInfoArg = 'astrofetch: error: argument -i/--info: invalid query'
exitBadSearch = (errShowUsage + invalidInfoArg)
   
def processInput(infoSupplied, useUnicode, printOutput):
    #Error handling
    if len(infoSupplied) > 2:
        exit(exitBadSearch)

    #1 arg = user likely searched starsign
    if len(infoSupplied) == 1: 
        infoSupplied = str(infoSupplied)
        formattedInfo = infoSupplied.lower().title()

        convertStarsignToDate(formattedInfo, useUnicode)

    #2 args = user likely searched date
    elif len(infoSupplied) == 2: 

        for info in infoSupplied:
            if info.isnumeric():
                formattedDay = info
            else:
                info = info[:3]
                formattedMonth = info.lower().title()

        try:
            convertDateToStarsign(formattedMonth, formattedDay, printOutput, useUnicode)
        except:
            exit(exitBadSearch)
    
def convertDateToStarsign(month, day, printOutput, useUnicode):
    monthSupplied = month[:3]
    daySupplied = day
    day30 = ['Feb', 'Apr', 'Jun', 'Sep', 'Nov']
    searchSuccess = False
    
    if int(daySupplied) > 31:
        exit(exitBadSearch)
    elif int(daySupplied) > 30 and monthSupplied in day30 or int(daySupplied) > 29 and monthSupplied == day30[0]:
        exit(exitBadSearch)
    
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
        exit(exitBadSearch)

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
        exit(exitBadSearch)

    if not useUnicode:
        print('\n'.join(resultForText))
    elif useUnicode:
        print(''.join(resultForUnicode))
