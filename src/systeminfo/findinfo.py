import os
import subprocess
import datetime
import tomllib

def getUser():
    user = os.environ['USER']
    return user

def getHost():
    with open("/etc/hostname", "r") as hostnameFile:
        host = hostnameFile.read()
    host = host.strip()
    return host

def getUptime():
    try:
        with open("/proc/uptime") as uptimeFile:
            uptime = uptimeFile.read().split(' ')[0]
    except:
        uptime = 'Unknown uptime!'
        return uptime

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
    try:
        with open("/etc/os-release") as distroFile:
            distroList = distroFile.read().split("\n")
    except:
        distro = 'Unknown distro!'
        return distro

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
    try:
        with open("/proc/sys/kernel/osrelease") as kernelFile:
            kernelInfo = kernelFile.read()
    except:
        kernelInfo = 'No kernel info found!'
        return kernelInfo

    kernelInfo = kernelInfo.strip().split('-')
    kernelVersion = kernelInfo.pop(0)

    uniqueKernel = ''
    for info in kernelInfo:
        match info:
            case 'lts':
                uniqueKernel = '-lts'
            case 'hardened':
                uniqueKernel = '-hardened'

    kernel = kernelVersion + uniqueKernel

    return kernel

def getDesktopEnv():
    desktopEnv = os.environ['DESKTOP_SESSION']

    match desktopEnv:
        case 'gnome':
            deVersion = subprocess.check_output(['gnome-shell', '--version']).decode('utf-8').rstrip()
            desktopEnv = deVersion.replace('Shell ', '')
        case 'plasmax11' | 'plasma':
            #using -v here takes too long, omit version
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
            desktopEnv = 'Cosmic DE'
        case _:
            desktopEnv = desktopEnv.lower().title()

    return desktopEnv

def getShell():
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
            currentShell = ' '.join(shell)
        case 'fish':
            shell = subprocess.check_output(['fish', '--version']).decode('utf-8').rstrip()
            currentShell = 'fish ' + shell.split(' ')[-1]
        case _:
            currentShell = shell

    return currentShell

def getMachineFamily():
    try:
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
        hardwareId = hardwareId.strip()
    except:
        hardwareId = 'Unknown hardware!'

    return hardwareId

def getDate():
    fulldate = datetime.datetime.now()
    month = fulldate.strftime("%B")         # = August
    day = fulldate.strftime("%d")           # = 27
    time = fulldate.strftime("%H:%M")       # = 10:45

    return month, day, time

def getMem(memType):
    try:
        with open("/proc/meminfo") as memoryInfoFile:
            memInfo = memoryInfoFile.read().split()
    except:
        memory = 'No memory info found!'
        return memory

    if memType == 'mem':
        totalMem = memInfo[1]
        availMem = memInfo[7]
    elif memType == 'swap':
        totalMem = memInfo[43]
        availMem = memInfo[46]

    memInfo = [totalMem, availMem]
    memoryGb = []

    for memValue in memInfo:
        memValue = round(int(memValue) / 1024000, 1)
        memoryGb.append(memValue)

    totalMem = round(memoryGb[0])
    availMem = memoryGb[1]

    if totalMem == round(availMem):
        usedMem = ''
        totalMem = str(totalMem) + 'GB'
    else:
        usedMem = totalMem - availMem
        totalMem = str(totalMem) + 'GB ('
        usedMem = '%.1f' % usedMem + "G used)"

    memory = totalMem + usedMem

    return memory

def getBlockSpace(block):
    TB = 1099511627776
    GB = 1073741824
    MB = 1048576

    partInfo = os.statvfs(block)

    partSizeBytes = partInfo.f_frsize * partInfo.f_blocks
    partFreeBytes = partInfo.f_frsize * partInfo.f_bfree

    if partSizeBytes < GB:
        partSize = round((partInfo.f_frsize * partInfo.f_blocks) / MB)
        partFree = round((partInfo.f_frsize * partInfo.f_bfree) / MB)
        partUnit = 'MB'
    elif partSizeBytes > TB:
        partSize = round((partInfo.f_frsize * partInfo.f_blocks) / TB)
        partFree = round((partInfo.f_frsize * partInfo.f_bfree) / TB)
        partUnit = 'TB'
    else:
        partSize = round((partInfo.f_frsize * partInfo.f_blocks) / GB)
        partFree = round((partInfo.f_frsize * partInfo.f_bfree) / GB)
        partUnit = 'GB'

    partUsed = partSize - partFree
    partSpace = str(partUsed) + partUnit + ' used, ' + str(partFree) + partUnit + ' free'

    return partSpace

def getCpuGpu():
    cpuName = ''
    gpuName = ''

    #CPU
    try:
        with open ("/proc/cpuinfo") as cpuFile:
            for line in cpuFile.readlines():
                if 'model name' in line:
                    cpuInfo = line.split(':')[1]
                    break
    except:
        cpuInfo = 'No CPU info found!'

    #Check cpu graphics
    if 'Graphics' in cpuInfo.title():
        gpuName = 'Integrated Graphics'

    #Remove extra words
    unnecessaryInfo = ['with','Processor']
    for word in unnecessaryInfo:
        if word in cpuInfo:
            cpuInfo = cpuInfo.split(word)[0]
    cpuInfo = cpuInfo.split()
    for word in cpuInfo:
        if 'Core' in word:
            word = ''
        cpuName = cpuName + word + ' '

    #GPU
    try:
        pciInfo = subprocess.check_output(['lspci']).decode('utf-8').rstrip().split('\n')
        for pciLine in pciInfo:
            pciLineContents = pciLine.split()

            gpuMarkers = ['VGA', '3D controller']
            for marker in gpuMarkers:
                if marker in pciLineContents:
                    if 'Integrated' in pciLineContents:
                        vgaInfo = ''
                        pass
                    else:
                        vgaInfo = pciLine
                        break

        if vgaInfo != '':
            gpuName = ''
            vgaInfo = vgaInfo.split('[')
            for section in vgaInfo:
                if ':' in section:
                    pass
                else:
                    if '(' in section:
                        section = section.split('(')[0]
                    gpuInfo = section.split('/')[0].replace(']', '')
                    gpuName = gpuName + gpuInfo + ' '
        elif vgaInfo == '' and gpuName == 'Integrated Graphics':
            pass
        else:
            gpuName = 'Unknown GPU'

    except:
        if gpuName != 'Integrated Graphics':
            gpuName = 'Unknown GPU!'

    return cpuName, gpuName

def getLocalIp():
    try:
        with open ("/proc/net/fib_trie") as ipInfoFile:
            ipInfo = ipInfoFile.read().split('|')
    except:
        localIp = 'No IP info found!'
        return localIp

    localIp = 'No connection'
    for ipInfoLine in ipInfo:
        if '32 host LOCAL' in ipInfoLine:
            if '127.0.0.1' in ipInfoLine:
                pass
            else:
                localIp = ipInfoLine
                break

    if localIp != 'No connection':
        localIp = localIp.split()[1]

    return localIp

def getSettings():
    #Check config file exists
    configFile = 'astrofetch.toml'
    srcDir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    parentDir = os.path.abspath(os.path.join(srcDir, os.pardir))
    configFile = os.path.abspath(os.path.join(parentDir, configFile))
    cantReadErr = 'astrofetch: cannot read config file'

    if not os.path.exists(configFile):
        print(cantReadErr)
        exit(configFile + ': file not found')

    try:
        with open(configFile, "rb") as settingsFile:
            settings = tomllib.load(settingsFile)
    except:
        print(cantReadErr)
        exit(configFile + ': incorrect format')

    globals = settings['Global']
    ruleset = settings['Entries']

    textColor = globals['textcolor']
    signColor = globals['logocolor']

    defaultRuleset = ruleset['default']
    customRuleset = ruleset['custom']

    #Assign ruleset
    if customRuleset:
        ruleset = customRuleset
    else:
        ruleset = defaultRuleset

    globalSettings = (textColor, signColor)

    return ruleset, globalSettings
