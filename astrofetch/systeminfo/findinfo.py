import os
import subprocess
import datetime

def getUser():
    user = os.environ['USER']
    return user

def getHost():
    with open("/etc/hostname", "r") as hostnameFile:
        host = hostnameFile.read()
    host = host.strip()
    return host

def getUptime():
    with open("/proc/uptime") as uptimeFile:
        uptime = uptimeFile.read().split(' ')[0]

    rawUptime = round(float(uptime))

    ONEMIN = 60
    ONEHOUR = 3600
    ONEDAY = 86400
    ONEWEEK = 604800
    ONEYEAR = 31556952

    if rawUptime <= ONEMIN:
        uptimeA = str(rawUptime) + " seconds"
        uptimeB = ''

    elif rawUptime <= ONEHOUR:
        upMinutes = divmod(rawUptime, ONEMIN)
        uptimeA = str(upMinutes[0]) + " minutes"
        uptimeB = ''

    elif rawUptime <= ONEDAY:
        upHours = divmod(rawUptime, ONEHOUR)
        upMinutes = divmod(upHours[1], ONEMIN)
        uptimeA = str(upHours[0]) + " hours"
        uptimeB = str(upMinutes[0]) + " minutes"

    elif rawUptime <= ONEWEEK:
        upDays = divmod(rawUptime, ONEDAY)
        upHours = divmod(upDays[1], ONEHOUR)
        uptimeA = str(upDays[0]) + " days"
        uptimeB = str(upHours[0]) + " hours"

    elif rawUptime <= ONEYEAR:
        upWeeks = divmod(rawUptime, ONEWEEK)
        upDays = divmod(upWeeks[1], ONEDAY)
        uptimeA = str(upWeeks[0]) + " weeks"
        uptimeB = str(upDays[0]) + " days"

    else:
        upYears = divmod(rawUptime, ONEYEAR)
        upDays = divmod(upYears[1], ONEDAY)
        uptimeA = str(upYears[0]) + " years"
        uptimeB = str(upDays[0]) + " days"

    totalUptime = [uptimeA, uptimeB]

    count = 0
    for value in totalUptime:
        if value[:2] == '1 ':
            totalUptime[count] = value[:-1]
        elif value[:2] == '0 ':
            totalUptime[count] = ''
        count = count + 1

    if totalUptime[1] == '':
        uptime = str(totalUptime[0])
    else:
        uptime = str(totalUptime[0]) + ', ' + str(totalUptime[1])

    return uptime

def getDistro():
    with open("/etc/os-release") as distroFile:
        distroList = distroFile.read().split("\n")

    NAME1 = distroList[0]
    NAME2 = distroList[1]

    if NAME1[:6] == "PRETTY":
        distro = NAME2
    elif NAME1[:3] == "BUG": #nix-specific
        distro = NAME1[-22:-15]
    else:
        distro = NAME1

    distro = distro.replace('NAME=', '')[1:-1]
    return distro

def getKernel():
    with open("/proc/sys/kernel/osrelease") as kernelFile:
        kernelVersion = kernelFile.read()
    
    kernel = kernelVersion.strip().split('-')[0]
    kernel = kernel.replace(".x86_64", '').replace(".aarch64", ' ')

    return kernel

def getDesktopEnv():
    desktopEnv = os.environ['DESKTOP_SESSION']
    match desktopEnv:
        case 'gnome':
            deVersion = subprocess.check_output(['gnome-shell', '--version']).decode('utf-8').rstrip()
            desktopEnv = deVersion.replace('Shell ', '')
        case 'plasmax11' | 'plasma':
            desktopEnv = 'KDE Plasma'
        case 'awesome':
            deVersion = subprocess.check_output(['awesome', '-v']).decode('utf-8').rstrip()
            deVersion = deVersion.split(' ')[1]
            desktopEnv = 'AwesomeWM ' + deVersion[1:]
        case 'xfce':
            deVersion = subprocess.check_output(['xfce4-session', '--version']).decode('utf-8').rstrip()
            deVersion = deVersion.split(' ')[1]
            desktopEnv = 'Xfce ' + deVersion
        case 'pop':
            desktopEnv = 'Cosmic'
        case _:
            if desktopEnv == '':
                desktopEnv = ' - '
            else:
                desktopEnv = desktopEnv.lower().title()

    return desktopEnv

def getShell():
    currentShell = ''

    shell = os.environ['SHELL']
    shell = shell.split('/')[-1]

    match shell:
        case 'bash':
            shell = subprocess.check_output(['bash', '--version']).decode('utf-8').rstrip()
            bashVersion = shell.split(' ')[3]
            bashVersionNumber = bashVersion.split('(')
            shell = bashVersionNumber[0]
            currentShell = 'bash ' + shell
        case 'zsh':
            shell = subprocess.check_output(['zsh', '--version']).decode('utf-8').rstrip()
            shell = shell.split(' ')[:-1]
            shell = ' '.join(shell)
            currentShell = currentShell + shell
        case 'fish':
            shell = subprocess.check_output(['fish', '--version']).decode('utf-8').rstrip()
            shell = 'fish ' + shell.split(' ')[-1]
            currentShell = currentShell + shell

    return currentShell

def getMachineFamily():
    with open("/sys/devices/virtual/dmi/id/product_family") as hardwareIdFile:
        hardwareId = hardwareIdFile.read().strip()
    if hardwareId == 'To be filled by O.E.M.':
        with open("/sys/devices/virtual/dmi/id/board_name") as boardIdFile:
            hardwareId = boardIdFile.read().strip()
            if hardwareId[-1] == ')':
                hardwareId = hardwareId.split('(')[0]
            hardwareId = hardwareId.lower().title()
    elif hardwareId == '':
        with open("/sys/devices/virtual/dmi/id/sys_vendor") as vendorIdFile:
            hardwareId = vendorIdFile.read().strip()

    return hardwareId

def getDate():
    fulldate = datetime.datetime.now()
    month = fulldate.strftime("%B")         # = August
    day = fulldate.strftime("%d")           # = 27
    time = fulldate.strftime("%H:%M")       # = 10:45
    return month, day, time

def getMem(memType):
    with open("/proc/meminfo") as memoryInfoFile:
        memInfo = memoryInfoFile.read().split()

    if memType == 'mem':
        totalMem = memInfo[1]
        usedMem = memInfo[4]
        cachedMem = memInfo[13]
    elif memType == 'swap':
        totalMem = memInfo[43]
        usedMem = memInfo[46]
        cachedMem = 0

    memInfo = [totalMem, usedMem, cachedMem]
    memoryGb = []

    for item in memInfo:
        item = int(item) / 1024000
        item = round(item, 1)
        memoryGb.append(item)

    totalMem = str(round(memoryGb[0])) + 'G ('
    usedMem = '%.1f' % (memoryGb[0] - memoryGb[1] - memoryGb[2])
    if usedMem[0] == '0':
        totalMem = totalMem[:-2]
        usedMem = ''
    else:
        usedMem = usedMem + "G used)"

    memory = totalMem + usedMem

    return memory
