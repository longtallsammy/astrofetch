colors = {'Yellow':'\033[93m', 'Green':'\033[32m', 'Red':'\033[31m', 'Brown':'\033[33m', 'Orange':'\033[91m', 'Pink':'\033[95m', 'Light-Green':'\033[92m', 'Purple':'\033[35m', 'Light-Blue':'\033[94m', 'Black':'\033[30m', 'Blue':'\033[34m', 'White':'\033[37m', 'Cyan':'\033[36m', 'Light-Cyan':'\033[96m'}

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
    colors.get('Green'))

leo = Starsign(
    'Leo', 
    '\u264c', 
    ['July', '23'],
    ['August', '22'], 
    'the Sun', 
    '\U0001F31E',
    'fire',
    'fixed',
    colors.get('Brown'))

virgo = Starsign(
    'Virgo', 
    '\u264d', 
    ['August', '23'], 
    ['September', '23'], 
    'Mercury', 
    '\U0001F680',
    'earth',
    'mutable',
    colors.get('Orange'))

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
    colors.get('Light-Green'))

sagittarius = Starsign(
    'Sagittarius', 
    '\u2650', 
    ['November', '22'], 
    ['December', '21'], 
    'Jupiter', 
    '\U0001F4A5',
    'fire',
    'mutable',
    colors.get('Pink'))

capricorn = Starsign(
    'Capricorn', 
    '\u2651',
    ['December', '22'],
    ['January', '19'], 
    'Saturn',
    '\U0001FA90',
    'earth',
    'cardinal',
    colors.get('Purple'))

aquarius = Starsign(
    'Aquarius',
    '\u2652', 
    ['January', '20'],
    ['February', '18'],
    'Uranus', 
    '\U0001F6F8',
    'air',
    'fixed',
    colors.get('Light-Blue'))

pisces = Starsign(
    'Pisces', 
    '\u2653', 
    ['February', '19'], 
    ['March', '19'], 
    'Neptune', 
    '\U0001F531',
    'water',
    'mutable',
    colors.get('Light-Green'))

signs = [aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces]
