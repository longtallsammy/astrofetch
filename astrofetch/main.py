from systeminfo import findinfo
from systeminfo import formatinfo
import build
from signs import starsigns
import search

def matchCliArgs(arguments):
    showResult = False
    useUnicode = False

    currentMonth, currentDay, currentTime = findinfo.getDate()
    currentSeason = search.convertDateToStarsign(currentMonth, currentDay, showResult, useUnicode)

    if arguments.small:
        build.smallFetch(formatinfo.smallFormat(currentSeason, arguments.unicode))
    elif arguments.mini:
        build.miniFetch(formatinfo.miniFormat(currentSeason, arguments.unicode))
    elif arguments.info:
        showResult = True
        search.processInput(arguments.info, arguments.unicode, showResult)
    elif arguments.verbose:
        build.fullFetch(currentSeason, formatinfo.verboseFormat(currentSeason))
    else:
        build.fullFetch(currentSeason, formatinfo.fullFormat(currentSeason))
