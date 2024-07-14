"""Hakerski slang, autor: Al Sweigart, al@inventwithpython.com
Zamienia litery w tekście na cyfry i inne znaki.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, dla początkujących, słowa"""

import random

try:
    import pyperclip  # Biblioteka pyperclip kopiuje tekst do schowka.
except ImportError:
    pass  # Jeśli biblioteka pyperclip nie jest zainstalowana, nic nie rób. To nie jest duży problem.


def main():
    print('''L3375P34]< (leetspeek)
autor: Al Sweigart, al@inventwithpython.com

Wpisz swoją wiadomość:''')
    english = input('> ')
    print()
    leetspeak = englishToLeetspeak(english)
    print(leetspeak)

    try:
        # Próba użycia biblioteki pyperclip spowoduje błąd NameError,
        # jeśli ta biblioteka nie została zaimportowana:
        pyperclip.copy(leetspeak)
        print('(Przekształcona wiadomość skopiowana do schowka).')
    except NameError:
        pass  # Nic nie rób, jeśli biblioteka pyperclip nie została zainstalowana.


def englishToLeetspeak(message):
    """ Wiadomość przekształca na slang hakerski."""
    # Upewnij się, że wszystkie klucze w słowniku kodów liter 'charMapping' są napisane z małej litery.
    charMapping = {
    'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
    'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
    'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
    'v': ['\\/']}
    leetspeak = ''
    for char in message:  # Sprawdź każdy znak:
        # Istnieje 70% szans, że zmienimy literę na inny znak.
        if char.lower() in charMapping and random.random() <= 0.70:
            possibleLeetReplacements = charMapping[char.lower()]
            leetReplacement = random.choice(possibleLeetReplacements)
            leetspeak = leetspeak + leetReplacement
        else:
            # Nie zmieniaj tej litery:
            leetspeak = leetspeak + char
    return leetspeak


# Jeśli program został uruchomiony (a nie zaimportowany), rozpocznij grę:
if __name__ == '__main__':
    main()
