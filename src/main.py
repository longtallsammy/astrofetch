from systeminfo import findinfo
from systeminfo import formatinfo
from signs import starsigns
import build
import search

def matchCliArgs(arguments):
    showResult = False
    useUnicode = False
    returnDate = True

    if not arguments.date:
        month, day, time = findinfo.getDate()
        season = search.convertDateToStarsign(month, day, showResult, useUnicode)
    else:
        month, day = search.processInput(arguments.date, arguments.unicode, showResult, returnDate)
        season = search.convertDateToStarsign(month, day, showResult, useUnicode)

    if arguments.mini:
        build.singleLine(formatinfo.miniFormat(season, arguments.unicode))
    elif arguments.small:
        build.singleLine(formatinfo.smallFormat(season, arguments.unicode))
    elif arguments.info:
        search.processInput(arguments.info, arguments.unicode, True, False)
    else:
        build.fullsize(season, formatinfo.largeFormat(season))
