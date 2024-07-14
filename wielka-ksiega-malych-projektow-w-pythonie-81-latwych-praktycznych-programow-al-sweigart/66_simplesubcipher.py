"""Prosty szyfr podstawieniowy, autor: Al Sweigart, al@inventwithpython.com
Prosty szyfr podstawieniowy ma przełożenie jeden do jednego
dla każdego symbolu w oryginalnym i zaszyfrowanym tekście.
Więcej informacji na stronie https://pl.wikipedia.org/wiki/Szyfr_podstawieniowy.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, kryptografia, matematyka"""

import random

try:
    import pyperclip  # Moduł pyperclip kopiuje tekst do schowka.
except ImportError:
    pass  # Jeśli moduł pyperclip nie jest zainstalowany, nic nie rób. To nie jest problem.

# Każdy możliwy symbol, który może być zaszyfrowany/odszyfrowany:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print('''Prosty szyfr podstawieniowy, autor: Al Sweigart
Prosty szyfr podstawieniowy ma przełożenie jeden do jednego
dla każdego symbolu w oryginalnym i zaszyfrowanym tekście.''')

    # Zapytaj użytkownika, czy chce zaszyfrować, czy odszyfrować wiadomość:
    while True:  # Pytaj, dopóki użytkownik nie wpisze z lub o.
        print('Chcesz (z)aszyfrować czy (o)dszyfrować?')
        response = input('> ').lower()
        if response.startswith('z'):
            myMode = 'zaszyfrowan'
            break
        elif response.startswith('o'):
            myMode = 'odszyfrowan'
            break
        print('Proszę, wpisz literę z lub o.')

    # Poproś użytkownika o podanie klucza:
    while True:  # Pytaj, dopóki użytkownik nie poda klucza.
        print('Podaj klucz.')
        if myMode == 'zaszyfrowan':
            print('Lub wpisz LOS, jeśli chcesz wygenerować losowy klucz.')
        response = input('> ').upper()
        if response == 'LOS':
            myKey = generateRandomKey()
            print('Twój klucz to: {}. ZACHOWAJ GO W TAJEMNICY!'.format(myKey))
            break
        else:
            if checkKey(response):
                myKey = response
                break

    # Spytaj użytkownika o wiadomość do zaszyfrowania/odszyfrowania:
    print('Wpisz wiadomość do {}ia.'.format(myMode))
    myMessage = input('> ')

    # Zaszyfruj/odszyfruj:
    if myMode == 'zaszyfrowan':
        translated = encryptMessage(myMessage, myKey)
    elif myMode == 'odszyfrowan':
        translated = decryptMessage(myMessage, myKey)

    # Wyświetl rezultat:
    print('Wiadomość po %siu brzmi:' % (myMode))
    print(translated)

    try:
        pyperclip.copy(translated)
        print('Pełny tekst %sej wiadomości został skopiowany do schowka.' % (myMode))
    except:
        pass  # Nic nie rób, jeśli moduł pyperclip nie został zaszyfrowany.


def checkKey(key):
    """Zwraca wartość True, jeśli klucz jest ważny. W przeciwnym razie zwraca wartość False."""
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        print('Wystąpił błąd w zestawie symboli lub w kluczu.')
        return False
    return True


def encryptMessage(message, key):
    """Zaszyfrowuje wiadomość za pomocą podanego klucza."""
    return translateMessage(message, key, 'szyfrowanie')


def decryptMessage(message, key):
    """Odszyfrowuje wiadomość za pomocą podanego klucza."""
    return translateMessage(message, key, 'odszyfrowanie')


def translateMessage(message, key, mode):
    """Zaszyfrowuje lub odszyfrowuje wiadomość za pomocą podanego klucza."""
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'odszyfrowanie':
        # W celu odszyfrowania wiadomości możemy wykorzystać ten sam kod co do szyfrowania. 
        # Musimy tylko zamienić miejscami łańcuchy znaków dla klucza i liter.
        charsA, charsB = charsB, charsA

    # Przejdź w pętli przez każdy znak w wiadomości:
    for symbol in message:
        if symbol.upper() in charsA:
            # Zaszyfruj/odszyfruj znak:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # Znak nie występuje w zmiennej LETTERS, więc dodaj go bez zmian.
            translated += symbol

    return translated


def generateRandomKey():
    """Generuje i zwraca losowy klucz szyfru."""
    key = list(LETTERS)  # Utwórz listę z łańcucha znaków LETTERS.
    random.shuffle(key)  # Potasuj listę.
    return ''.join(key)  # Utwórz z listy łańcuch znaków.


# Jeśli program został uruchomiony (a nie zaimportowany), wykonaj go:
if __name__ == '__main__':
    main()
