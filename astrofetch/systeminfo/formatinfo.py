import datetime
from systeminfo import findinfo
from signs import starsigns

user = findinfo.getUser()
host = findinfo.getHost()
userhost = (user + '@' + host)
uptime = findinfo.getUptime()
month, day, time = findinfo.getDate()
distro = findinfo.getDistro()
kernel = findinfo.getKernel()
shell = findinfo.getShell()
machine = findinfo.getMachineFamily()
desktop = findinfo.getDesktopEnv()
memory = findinfo.getMem('mem')
swap = findinfo.getMem('swap')
home = findinfo.getBlockSpace('/home')
boot = findinfo.getBlockSpace('/boot')
cpu, gpu = findinfo.getCpuGpu()
localIp = findinfo.getLocalIp()

def boldenText(text, color):
    text = color + '\033[1m' + text + '\033[0m'
    return text

def fullFormat(sign): #organize this so its quicker, ur running 2 ifs. match maybe
    if len(userhost) > len(month + day + time) + 9:
        dashline = ('-' * (len(userhost)))
    elif len(uptime) + 8 > len(month + day + time) + 9:
        dashline = ('-' * (len(uptime) + 8 ))
    else:
        dashline = ('-' * (len(month + day + time) + 9))
    if len(machine) + 9 > len(dashline):
        dashline = ('-' * (len(machine) + 9))
    elif len(kernel) + 9 > len(dashline):
        dashline = ('-' * (len(kernel) + 9))

    systemPortion = (
        boldenText(userhost, sign.color),
        dashline,
        boldenText('Date: ', sign.color) + month + ' ' + day + ', ' + time, 
        dashline, 
        boldenText('OS: ', sign.color) + distro, 
        boldenText('Kernel: ', sign.color) + kernel, 
        boldenText('Uptime: ', sign.color) + uptime, 
        boldenText('Shell: ', sign.color) + shell,
        boldenText('DE: ', sign.color) + desktop,
        boldenText('Machine: ', sign.color) + machine,
        dashline)

    astrologyPortion = (
        boldenText('Season: ', sign.color) + sign.name, 
        boldenText('Starts: ', sign.color) + sign.startmonth + ' ' + sign.startday, 
        boldenText('Ends: ', sign.color) + sign.endmonth + ' ' + sign.endday, 
        boldenText('Planet: ', sign.color) + sign.planet.title(), 
        boldenText('Element: ', sign.color) + sign.element.title(), 
        boldenText('Modality: ', sign.color) + sign.modality.title())

    formattedSystemInfo = (systemPortion + astrologyPortion)

    return formattedSystemInfo

def verboseFormat(sign):
    if len(userhost) > len(month + day + time) + 9:
        dashline = ('-' * (len(userhost)))
    elif len(uptime) + 8 > len(month + day + time) + 9:
        dashline = ('-' * (len(uptime) + 8 ))
    else:
        dashline = ('-' * (len(month + day + time) + 9))
    if len(machine) + 9 > len(dashline):
        dashline = ('-' * (len(machine) + 9))
    elif len(kernel) + 9 > len(dashline):
        dashline = ('-' * (len(kernel) + 9))

    systemPortion = (
        boldenText(userhost, sign.color),
        dashline,
        boldenText('Date: ', sign.color) + month + ' ' + day + ', ' + time, 
        boldenText('Season: ', sign.color) +  sign.name,
        dashline, 
        boldenText('OS: ', sign.color) + distro, 
        boldenText('Kernel: ', sign.color) + kernel, 
        boldenText('Uptime: ', sign.color) + uptime, 
        boldenText('Shell: ', sign.color) + shell,
        boldenText('DE: ', sign.color) + desktop,
        boldenText('Machine: ', sign.color) + machine)

    verbosePortion = (
        boldenText('Memory: ', sign.color) + memory, 
        boldenText('CPU: ', sign.color) + cpu, 
        boldenText('GPU: ', sign.color) + gpu,
        boldenText('Home: ', sign.color) + home,
        boldenText('Boot: ', sign.color) + boot,
        boldenText('Local Addr: ', sign.color) + localIp,
    )

    formattedSystemInfo = (systemPortion + verbosePortion)

    return formattedSystemInfo

def smallFormat(sign, useUnicode):
    if not useUnicode:
        formattedSystemInfo = (
            time + 
            ' ' + 
            str(month + ' ' + day) + 
            ', ' + 
            sign.name + 
            ' season.')
    else:
        formattedSystemInfo = (
            time +
            ' ' +
            sign.emoji)

    return formattedSystemInfo

def miniFormat(sign, useUnicode):
    if not useUnicode:
        formattedSystemInfo = sign.name
    else: 
        formattedSystemInfo = sign.emoji

    return formattedSystemInfo
