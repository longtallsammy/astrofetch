import os
import subprocess
import datetime
import tomllib

def getUser():
    user = os.environ['USER']
    return user

def getHost():
    try:
        with open("/etc/hostname", "r") as hostnameFile:
            host = hostnameFile.read()
    except FileNotFoundError:
        host = 'Unknown hostname'
        return host

    host = host.strip()
    return host

def getUptime():
    try:
        with open("/proc/uptime") as uptimeFile:
            uptime = uptimeFile.read().split(' ')[0]
    except FileNotFoundError:
        uptime = 'Unknown uptime!'
        return uptime

    uptimeSeconds = round(float(uptime))

    ONEMIN = 60
    ONEHOUR = 3600
    ONEDAY = 86400
    ONEWEEK = 604800
    ONEYEAR = 31556952

    if uptimeSeconds <= ONEMIN:
        uptimeA = ' '.join([str(uptimeSeconds), "seconds"])
        uptimeB = ''

    elif uptimeSeconds <= ONEHOUR:
        upMinutes = divmod(uptimeSeconds, ONEMIN)
        uptimeA = ' '.join([str(upMinutes[0]), "minutes"])
        uptimeB = ''

    elif uptimeSeconds <= ONEDAY:
        upHours = divmod(uptimeSeconds, ONEHOUR)
        upMinutes = divmod(upHours[1], ONEMIN)
        uptimeA = ' '.join([str(upHours[0]), "hours"])
        uptimeB = ' '.join([str(upMinutes[0]),  "minutes"])

    elif uptimeSeconds <= ONEWEEK:
        upDays = divmod(uptimeSeconds, ONEDAY)
        upHours = divmod(upDays[1], ONEHOUR)
        uptimeA = ' '.join([str(upDays[0]), "days"])
        uptimeB = ' '.join([str(upHours[0]), "hours"])

    elif uptimeSeconds <= ONEYEAR:
        upWeeks = divmod(uptimeSeconds, ONEWEEK)
        upDays = divmod(upWeeks[1], ONEDAY)
        uptimeA = ' '.join([str(upWeeks[0]), "weeks"])
        uptimeB = ' '.join([str(upDays[0]), "days"])

    else:
        upYears = divmod(uptimeSeconds, ONEYEAR)
        upDays = divmod(upYears[1], ONEDAY)
        uptimeA = ' '.join([str(upYears[0]), "years"])
        uptimeB = ' '.join([str(upDays[0]) + "days"])

    totalUptime = [uptimeA, uptimeB]

    #Format result
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
        uptime = ', '.join([str(totalUptime[0]), str(totalUptime[1])])

    return uptime

def getDistro():
    try:
        with open("/etc/os-release") as distroFile:
            distroList = distroFile.read().split("\n")
    except FileNotFoundError:
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
    except FileNotFoundError:
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

    kernel = ''.join([kernelVersion + uniqueKernel])

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

    #Get shell version
    match shell:
        case 'bash':
            shell = subprocess.check_output(['bash', '--version']).decode('utf-8').rstrip()
            bashVersion = shell.split(' ')[3]
            bashVersionNumber = bashVersion.split('(')
            shell = bashVersionNumber[0]
            currentShell = ' '.join(['bash' + shell])
        case 'zsh':
            shell = subprocess.check_output(['zsh', '--version']).decode('utf-8').rstrip()
            shell = shell.split(' ')[:-1]
            currentShell = ' '.join(shell)
        case 'fish':
            shell = subprocess.check_output(['fish', '--version']).decode('utf-8').rstrip()
            currentShell = ' '.join(['fish' + shell.split(' ')[-1]])
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
    except FileNotFoundError:
        hardwareId = 'Unknown hardware!'

    return hardwareId

def getDate():
    fulldate = datetime.datetime.now()
    month = fulldate.strftime("%B")#August
    day = fulldate.strftime("%d")#27
    time = fulldate.strftime("%H:%M")#10:45

    return month, day, time

def getMem(memType):
    try:
        with open("/proc/meminfo") as memoryInfoFile:
            memInfo = memoryInfoFile.read().split()
    except FileNotFoundError:
        memory = 'No memory info found!'
        return memory

    if memType == 'mem':
        totalMem = memInfo[1]
        availMem = memInfo[7]
    elif memType == 'swap':
        totalMem = memInfo[43]
        availMem = memInfo[46]

    #Convert to readable units
    memoryGb = [round(int(totalMem) / 1024000), round(int(availMem) / 1024000, 1)]

    totalMem = memoryGb[0]
    availMem = memoryGb[1]

    #Only show used memory if memory is being used
    if totalMem == round(availMem):
        usedMem = ''
        totalMem = ''.join([str(totalMem), 'GB'])
    else:
        usedMem = totalMem - availMem
        totalMem = ''.join([str(totalMem), 'GB ('])
        usedMem = '%.1f' % usedMem + "G used)"

    memory = ''.join([totalMem, usedMem])

    return memory

def getBlockSpace(block):
    TB = 1099511627776
    GB = 1073741824
    MB = 1048576

    partInfo = os.statvfs(block)

    #Convert to readable units
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
    partSpace = ' '.join([str(partUsed) + partUnit, 'used,', str(partFree) + partUnit, 'free'])

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
    except FileNotFoundError:
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

            #Get VGA section of lspci output
            gpuMarkers = ['VGA', '3D controller']
            for marker in gpuMarkers:
                if marker in pciLineContents:
                    if 'Integrated' in pciLineContents: #ignore it
                        vgaInfo = ''
                        pass
                    else:
                        vgaInfo = pciLine
                        break

        if vgaInfo != '': #lspci succeeded
            gpuName = ''
            vgaInfo = vgaInfo.split('[')
            for section in vgaInfo:
                if ':' in section: #first half, ignore it
                    pass
                else: #second half, contains gpu name
                    if '(' in section: #rev section, ignore it
                        section = section.split('(')[0]

                    #Format gpu name
                    gpuInfo = section.split('/')[0].replace(']', '')
                    gpuName = ''.join([gpuName, gpuInfo + ' '])

        elif vgaInfo == '' and gpuName == 'Integrated Graphics': #lspci failed
            pass
        else: #CPU graphics check failed too
            gpuName = 'Unknown GPU'

    except:
        if gpuName != 'Integrated Graphics':
            gpuName = 'Unknown GPU!'

    return cpuName, gpuName

def getLocalIp():
    try:
        with open ("/proc/net/fib_trie") as ipInfoFile:
            ipInfo = ipInfoFile.read().split('|')
    except FileNotFoundError:
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
    configFile = 'astrofetch.toml'
    srcDir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    parentDir = os.path.abspath(os.path.join(srcDir, os.pardir))
    configFile = os.path.abspath(os.path.join(parentDir, configFile))
    cantReadErr = 'astrofetch: cannot read config file'

    #Check config file exists
    if not os.path.exists(configFile):
        print(cantReadErr)
        exit(configFile + ': file not found')

    try:
        with open(configFile, "rb") as settingsFile:
            settings = tomllib.load(settingsFile)
    except tomllib.TOMLDecodeError:
        print(cantReadErr)
        exit(configFile + ': incorrect format')
    except FileNotFoundError:
        print(cantReadErr)
        exot(configFile + ': file not found')

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
