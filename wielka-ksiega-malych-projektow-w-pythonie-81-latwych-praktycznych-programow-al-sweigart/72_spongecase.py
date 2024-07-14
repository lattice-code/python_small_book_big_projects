"""tEkSt KaNcIaStOpOrTy, autor: Al Sweigart, al@inventwithpython.com
Zamienia podany tekst na tEkSt KaNcIaStOpOrTy.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, dla początkujących, słowa"""

import random

try:
    import pyperclip  # Moduł pyperclip kopiuje tekst do schowka.
except ImportError:
    pass  # Jeśli moduł pyperclip nie jest zainstalowany, nic nie rób. To nie stanowi problemu.


def main():
    """Uruchamia program Tekst kanciastoporty."""
    print('''tEkSt KaNcIaStOpOrTy, aUtOr: aL sWeIGaRt, Al@iNvEnTwItHpYtHoN.cOm

wPiSz SwÓj TeKsT:''')
    spongecase = englishToSpongecase(input('> '))
    print()
    print(spongecase)

    try:
        pyperclip.copy(spongecase)
        print('(sKoPiOwAnO dO sChOwKa.)')
    except:
        pass  # Nie nie rób, jeśli moduł pyperclip nie został zainstalowany.


def englishToSpongecase(message):
    """Zwraca tekst w stylu memu ze SpongeBobem."""
    spongecase = ''
    useUpper = False

    for character in message:
        if not character.isalpha():
            spongecase += character
            continue

        if useUpper:
            spongecase += character.upper()
        else:
            spongecase += character.lower()

        # W 90% przypadków małe i wielkie litery występują naprzemiennie.
        if random.randint(1, 100) <= 90:
            useUpper = not useUpper  # Zmień wielkość litery.
    return spongecase


# Jeśli ten program został uruchomiony (a nie zaimportowany), wykonaj go:
if __name__ == '__main__':
    main()
