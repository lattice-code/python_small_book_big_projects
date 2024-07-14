"""Magiczna kryształowa kula, autor: Al Sweigart, al@inventwithpython.com
Zadaj pytanie typu tak/nie dotyczące Twojej przyszłości. Program inspirowany magiczną kulą nr 8.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, dla początkujących, zabawny"""

import random, time


def slowSpacePrint(text, interval=0.1):
    """Wyświetla powoli tekst, 
    w którym każda litera jest oddzielona spacją, a litery I są napisane małą literą."""
    for character in text:
        if character == 'I':
            # Litery I wyświetlane są małymi literami:
            print('i ', end='', flush=True)
        else:
            # Inne znaki są wyświetlane normalnie:
            print(character + ' ', end='', flush=True)
        time.sleep(interval)
    print()  # Na końcu wyświetl dwa znaki nowej linii.
    print()


# Poproś o zadanie pytania:
slowSpacePrint('MAGICZNA KRYSZTAŁOWA KULA, AUTOR: AL SWEiGART')
time.sleep(0.5)
slowSpacePrint('ZADAJ PYTANIE, NA KTÓRE ODPOWIEDŹ BRZMI TAK LUB NIE.')
input('> ')

# Wyświetl krótką odpowiedź:
replies = [
    'NIECH POMYŚLĘ...',
    'CIEKAWE PYTANIE...',
    'HM... JESTEŚ PEWIEN, ŻE CHCESZ WIEDZIEĆ...?',
    'NIE SĄDZISZ, ŻE LEPIEJ NIE WIEDZIEĆ O PEWNYCH SPRAWACH...?',
    'MOGĘ CI POWIEDZIEĆ, ALE OBAWIAM SIĘ, ŻE ODPOWIEDŹ CI SIĘ NIE SPODOBA...',
    'TAK... NIE... MOŻE... POMYŚLĘ O TYM...',
    'I CO ZORBISZ, GDY POZNASZ ODPOWIEDŹ? ZASTANÓWMY SIĘ...',
    'MUSZĘ SIĘ NARADZIĆ...',
    'MUSISZ USIĄŚĆ PRZED USŁYSZENIEM ODPOWIEDZI...',
]
slowSpacePrint(random.choice(replies))

# Dramatyczna przerwa:
slowSpacePrint('.' * random.randint(4, 12), 0.7)

# Podaj odpowiedź:
slowSpacePrint('MAM ODPOWIEDŹ...', 0.2)
time.sleep(1)
answers = [
    'TAK, NA PEWNO',
    'MOJA ODPOWIEDŹ BRZMI NIE',
    'ZAPYTAJ MNIE PÓŹNIEJ',
    'JESTEM ZAPROGRAMOWNANA, BY ODPOWIADAĆ TAK',
    'GWIAZDY MÓWIĄ TAK, ALE JA MÓWIĘ NIE',
    'MOŻE, NIE WIEM',
    'SKUP SIĘ I ZADAJ PYTANIE JESZCZE RAZ',
    'WĄTPLIWE, BARDZO WĄTPLIWE',
    'ODPOWIEDŹ TWIERDZĄCA',
    'TAK, CHOĆ MOŻE CI SIĘ TO NIE PODOBAĆ',
    'NIE, MIMO ŻE WOLAŁBYŚ INNĄ ODPOWIEDŹ',
]
slowSpacePrint(random.choice(answers), 0.05)
