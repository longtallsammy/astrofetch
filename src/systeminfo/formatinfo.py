import datetime
from systeminfo import findinfo
from signs import starsigns

configFile = 'astrofetch.toml'
configErrMsg = ("astrofetch: error in config file '" + configFile + "'")
configInvalidMsg = (configFile + ": invalid entry '")

month, day, time = findinfo.getDate()
date = ' '.join([month, day + ',', time])

def boldenText(text, color):
    text = ''.join([color + '\033[1m' + text + '\033[0m'])
    return text

def largeFormat(sign):
    #Get settings, process globals
    ruleset, globalSettings = findinfo.getSettings()
    textColorSetting, logoColorSetting = globalSettings[0], globalSettings[1]

    textColor = sign.color

    for colorSetting in [textColorSetting, logoColorSetting]:
        if colorSetting != 'default':
            if colorSetting in starsigns.colors:
                color = starsigns.colors.get(colorSetting)
            else:
                print(configErrMsg)
                exit(configInvalidMsg + colorSetting + "'")

            if colorSetting == logoColorSetting:
                sign.color = color
            elif colorSetting == textColorSetting:
                textColor = color

    #Assign field prefixes
    systemInfo = {
        'User: ': findinfo.getUser(),
        'Hostname: ': findinfo.getHost(),
        'Uptime: ': findinfo.getUptime(),
        'Date: ': date,
        'OS: ': findinfo.getDistro(),
        'Kernel: ': findinfo.getKernel(),
        'Shell: ': findinfo.getShell(),
        'Machine: ': findinfo.getMachineFamily(),
        'DE: ': findinfo.getDesktopEnv(),
        'Memory: ': findinfo.getMem('mem'),
        'Swap: ': findinfo.getMem('swap'),
        'Home: ': findinfo.getBlockSpace('/home'),
        'Boot: ': findinfo.getBlockSpace('/boot'),
        'CPU: ': findinfo.getCpuGpu()[0],
        'GPU: ': findinfo.getCpuGpu()[1],
        'IP: ': findinfo.getLocalIp(),
        'Season: ': sign.name,
        'Starts: ': sign.startmonth + ' ' + sign.startday,
        'Ends: ': sign.endmonth + ' ' + sign.endday,
        'Planet: ': sign.planet.title(),
        'Element: ': sign.element.title(),
        'Modality: ': sign.modality.title()
    }

    #Process user settings
    largeFormatInfo = []
    dashlineLength = 0

    for item in ruleset:
        if item in ['cpu', 'gpu', 'ip', 'de', 'os']:
            item = ''.join([item.upper(), ': '])
        else:
            item = ''.join([item.replace('season-', '').title(), ': '])

        if item in systemInfo.keys():
            #assign separator length
            itemLength = len(item + systemInfo.get(item))
            if itemLength >= dashlineLength:
                dashlineLength = itemLength + 1
            #assign color
            entry = boldenText(item, textColor) + systemInfo.get(item)
            largeFormatInfo.append(entry)
        else:
            match item:
                #exceptions & errors
                case 'Separator: ':
                    largeFormatInfo.append(item)
                case 'Userhost: ':
                    userhost = '@'.join([systemInfo.get('User: '), systemInfo.get('Hostname: ')])
                    largeFormatInfo.append(boldenText(userhost, textColor))
                case _:
                    print(configErrMsg)
                    exit(configInvalidMsg + item.lower()[:-2] + "'")

    #separators
    count = 0
    for item in largeFormatInfo:
        if item == 'Separator: ':
            largeFormatInfo[count] = '-' * dashlineLength
        count = count + 1

    return largeFormatInfo

def smallFormat(sign, useUnicode):
    if not useUnicode:
        formattedSystemInfo = ' '.join([date + ',', sign.name, 'season.'])
    else:
        formattedSystemInfo = ' '.join([time + ' ' + sign.emoji])

    return formattedSystemInfo

def miniFormat(sign, useUnicode):
    if not useUnicode:
        formattedSystemInfo = sign.name
    else:
        formattedSystemInfo = sign.emoji

    return formattedSystemInfo
