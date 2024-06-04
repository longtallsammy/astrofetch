import argparse

errorMsg = 'see astrofetch -h for usage'
argComboErr = 'astrofetch: invalid combination of arguments'
unicodeErr = 'astrofetch: invalid use cannot show date as unicode'

parser = argparse.ArgumentParser(
    prog='astrofetch',
    description='Fetch program to display the current zodiac season and system information.',
    epilog=f"NOTE: -u cannot be used alone. It must accompany -s, -i or -m", formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument(
    '-s', '--small', 
    action='store_true', 
    help='show information on a single line')
parser.add_argument(
    '-m', '--mini', 
    action='store_true', 
    help='show as little information as possible')
parser.add_argument(
    '-u', '--unicode', 
    action='store_true', 
    default=False, 
    help='use unicode characters where possible')
parser.add_argument(
    '-i', '--info', 
    nargs='+', 
    metavar='', 
    help='search for sign or date information (eg: leo) (jan 1)')
parser.add_argument(
    '-v', '--verbose',
    action='store_true',
    help='show more system specs')

args = parser.parse_args()

if args.small:
    if args.mini or args.info:
        print(argComboErr)
        exit(errorMsg)
if args.mini:
    if args.info:
        print(argComboErr)
        exit(errorMsg)
if args.verbose:
    if args.info or args.mini or args.small:
        print(argComboErr)
        exit(errorMsg)
