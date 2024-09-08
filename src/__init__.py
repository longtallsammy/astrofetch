import sys
import platform

if platform.system() != 'Linux':
    exit("Astrofetch is only supported on Linux!")

requiredMajor = 3
requiredMinor = 11

versionMajor = sys.version_info.major
versionMinor = sys.version_info.minor

if versionMajor < requiredMajor or versionMajor == requiredMajor and versionMinor < requiredMinor:
    exit("Python version 3.11 or higher required")

import parsecli
import main

main.matchCliArgs(parsecli.args)
