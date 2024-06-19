colors = {'Black':'\033[38;2;51;51;49m',
          'Grey':'\033[38;2;206;208;183m',
          'Red':'\033[38;2;209;74;74m',
          'Orange':'\033[38;2;239;158;66m',
          'Mint':'\033[38;2;141;206;139m',
          'Green':'\033[38;2;89;165;66m',
          'Brown':'\033[38;2;178;128;104m',
          'Yellow':'\033[38;2;238;229;111m',
          'Blue':'\033[38;2;83;146;202m',
          'Purple':'\033[38;2;196;150;222m',
          'Pink':'\033[38;2;238;131;220m',
          'Beige':'\033[38;2;238;189;146m',
          'Salmon':'\033[38;2;245;107;107m',
          'Dark-Blue':'\033[38;2;42;78;131m',
          'White':'\033[38;2;205;213;226m'}

class Starsign:
    def __init__(sign, name, emoji, startdate, enddate, planet, pmoji, element, modality, color):
        sign.name = name
        sign.emoji = emoji
        sign.startmonth = startdate[0]
        sign.startday = startdate[1]
        sign.endmonth = enddate[0]
        sign.endday = enddate[1]
        sign.planet = planet
        sign.pmoji = pmoji
        sign.element = element
        sign.modality = modality
        sign.color = color

    def __str__(sign):
        return f"{sign.name} season runs from {sign.startmonth} {sign.startday} to {sign.endmonth} {sign.endday}."
    
    def getValue(sign, grouplist, emojidict):
        for groupname, group in grouplist.items():
           for star in group:
                if star == sign:
                    if not emojidict:
                        return groupname
                    else:
                        for emoji, emojiname in emojidict.items():
                            if groupname == emojiname:
                                return emoji

aries = Starsign(
    'Aries',
    '\u2648',
    ['March', '20'],
    ['April', '18'],
    'Mars',
    '\U0001F33A',
    'fire',
    'cardinal',
    colors.get('Red'))

taurus = Starsign(
    'Taurus',
    '\u2649',
    ['April', '19'],
    ['May', '20'],
    'Venus',
    '\U0001F338',
    'earth',
    'fixed',
    colors.get('Green'))

gemini = Starsign(
    'Gemini',
    '\u264a',
    ['May', '21'],
    ['June', '20'],
    'Mercury',
    '\U0001F680',
    'air',
    'mutable',
    colors.get('Yellow'))

cancer = Starsign(
    'Cancer',
    '\u264b',
    ['June', '21'],
    ['July', '22'],
    'the Moon',
    '\U0001F31A',
    'water',
    'cardinal',
    colors.get('Grey'))

leo = Starsign(
    'Leo',
    '\u264c',
    ['July', '23'],
    ['August', '22'],
    'the Sun',
    '\U0001F31E',
    'fire',
    'fixed',
    colors.get('Orange'))

virgo = Starsign(
    'Virgo',
    '\u264d',
    ['August', '23'],
    ['September', '23'],
    'Mercury',
    '\U0001F680',
    'earth',
    'mutable',
    colors.get('Brown'))

libra = Starsign(
    'Libra',
    '\u264e',
    ['September', '23'],
    ['October', '22'],
    'Venus',
    '\U0001F338',
    'air',
    'cardinal',
    colors.get('Pink'))

scorpio = Starsign(
    'Scorpio',
    '\u264f',
    ['October', '23'],
    ['November', '21'],
    'Pluto',
    '\U0001F311',
    'water',
    'fixed',
    colors.get('Dark-Blue'))

sagittarius = Starsign(
    'Sagittarius',
    '\u2650',
    ['November', '22'],
    ['December', '21'],
    'Jupiter',
    '\U0001F4A5',
    'fire',
    'mutable',
    colors.get('Purple'))

capricorn = Starsign(
    'Capricorn', 
    '\u2651',
    ['December', '22'],
    ['January', '19'], 
    'Saturn',
    '\U0001FA90',
    'earth',
    'cardinal',
    colors.get('Salmon'))

aquarius = Starsign(
    'Aquarius',
    '\u2652',
    ['January', '20'],
    ['February', '18'],
    'Uranus',
    '\U0001F6F8',
    'air',
    'fixed',
    colors.get('Blue'))

pisces = Starsign(
    'Pisces',
    '\u2653',
    ['February', '19'],
    ['March', '19'],
    'Neptune',
    '\U0001F531',
    'water',
    'mutable',
    colors.get('Mint'))

signs = [aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces]
