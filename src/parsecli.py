import argparse
import os.path

configFile = 'astrofetch.toml'

errorMsg = 'see astrofetch -h for usage'
argComboErr = 'astrofetch: invalid combination of arguments'
unicodeErr = 'astrofetch: invalid use cannot show date as unicode'
noSettingsErr = 'astrofetch: missing config file ' + configFile

configFileExists = os.path.exists('../' + configFile)

parser = argparse.ArgumentParser(
    prog='astrofetch',
    description='Fetch program to display the current zodiac season and system information.',
    epilog=f"Config: file 'astrofetch.toml' must be present when using formats which display a logo", formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument(
    '-s', '--small',
    action='store_true',
    help='format information to a single line')
parser.add_argument(
    '-m', '--mini',
    action='store_true',
    help='only show current sign')
parser.add_argument(
    '-u', '--unicode',
    action='store_true',
    default=False,
    help='use unicode characters')
parser.add_argument(
    '-i', '--info',
    nargs='+',
    metavar='',
    help='search for a sign or date information (eg: leo // jan 1)')
parser.add_argument(
    '-d', '--date',
    nargs='+',
    metavar='',
    help='use logo of season belonging to date (eg: jan 1)')

args = parser.parse_args()

#Conflicting arguments
if args.small:
    if args.mini or args.info or args.date:
        print(argComboErr)
        exit(errorMsg)
if args.mini:
    if args.info or args.date:
        print(argComboErr)
        exit(errorMsg)
if args.info:
    if args.date:
        print(argComboErr)
        exit(errorMsg)
else:
    if not configFileExists:
        print(noSettingsErr)
        exit(errorMsg)
