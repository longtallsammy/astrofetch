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
    '\033[31m')

taurus = Starsign(
    'Taurus', 
    '\u2649', 
    ['April', '19'], 
    ['May', '20'], 
    'Venus', 
    '\U0001F338',
    'earth',
    'fixed',
    '\033[32m')

gemini = Starsign(
    'Gemini', 
    '\u264a', 
    ['May', '21'], 
    ['June', '20'], 
    'Mercury', 
    '\U0001F680',
    'air',
    'mutable',
    '\033[93m')

cancer = Starsign(
    'Cancer',
    '\u264b', 
    ['June', '21'], 
    ['July', '22'], 
    'the Moon', 
    '\U0001F31A',
    'water',
    'cardinal',
    '\033[32m')

leo = Starsign(
    'Leo', 
    '\u264c', 
    ['July', '23'],
    ['August', '22'], 
    'the Sun', 
    '\U0001F31E',
    'fire',
    'fixed',
    '\033[33m')

virgo = Starsign(
    'Virgo', 
    '\u264d', 
    ['August', '23'], 
    ['September', '23'], 
    'Mercury', 
    '\U0001F680',
    'earth',
    'mutable',
    '\033[91m')

libra = Starsign(
    'Libra', 
    '\u264e', 
    ['September', '23'], 
    ['October', '22'], 
    'Venus', 
    '\U0001F338',
    'air',
    'cardinal',
    '\033[95m')

scorpio = Starsign(
    'Scorpio', 
    '\u264f', 
    ['October', '23'], 
    ['November', '21'], 
    'Pluto', 
    '\U0001F311',
    'water',
    'fixed',
    '\033[92m')

sagittarius = Starsign(
    'Sagittarius', 
    '\u2650', 
    ['November', '22'], 
    ['December', '21'], 
    'Jupiter', 
    '\U0001F4A5',
    'fire',
    'mutable',
    '\033[95m')

capricorn = Starsign(
    'Capricorn', 
    '\u2651',
    ['December', '22'],
    ['January', '19'], 
    'Saturn',
    '\U0001FA90',
    'earth',
    'cardinal',
    '\033[35m')

aquarius = Starsign(
    'Aquarius',
    '\u2652', 
    ['January', '20'],
    ['February', '18'],
    'Uranus', 
    '\U0001F6F8',
    'air',
    'fixed',
    '\033[94m')

pisces = Starsign(
    'Pisces', 
    '\u2653', 
    ['February', '19'], 
    ['March', '19'], 
    'Neptune', 
    '\U0001F531',
    'water',
    'mutable',
    '\033[92m')

signs = [aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces]
