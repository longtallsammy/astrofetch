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
    with open ("/proc/cpuinfo") as cpuFile:
        for line in cpuFile.readlines():
            if 'model name' in line:
                cpuInfo = line.split(':')[1]
                break

    #Checking if cpu has graphics
    if 'Graphics' in cpuInfo.title():
        gpuName = 'Integrated Graphics'

    unnecessaryInfo = ['with','Processor']
    for separator in unnecessaryInfo:
        if separator in cpuInfo:
            cpuInfo = cpuInfo.split(separator)[0]

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
            gpuName = 'Unknown GPU'

    return cpuName, gpuName

def getLocalIp():
    with open ("/proc/net/fib_trie") as ipInfoFile:
        for ipInfoLine in ipInfoFile.read().split('|'):
            if '32 host LOCAL' in ipInfoLine:
                if '127.0.0.1' in ipInfoLine:
                    pass
                else:
                    localIp = ipInfoLine
                    break

    if localIp != '':
        localIp = localIp.split()[1]
    else:
        localIp = ' -127.0.0.1- '

    return localIp
