"""Świńska łacina, autor: Al Sweigart, al@inventwithpython.com
Zamienia wiadomość na świńską łacinę.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, słowa"""

try:
    import pyperclip  # Moduł pyperclip kopiuje tekst do schowka.
except ImportError:
    pass  # Jeśli moduł pyperclip nie jest zainstalowany, nic się nie dzieje. Jego brak nie stanowi problemu.

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')


def main():
    print('''Świńska łacina
autor: Al Sweigart, al@inventwithpython.com

Wpisz swoją wiadomość:''')
    pigLatin = englishToPigLatin(input('> '))

    # Połącz wszystkie słowa z powrotem w jeden łańcuch znaków:
    print(pigLatin)

    try:
        pyperclip.copy(pigLatin)
        print('(Skopiowano wiadomość w świńskiej łacinie do schowka.)')
    except NameError:
        pass  # Nic nie rób, jeśli moduł pyperclip nie jest zainstalowany.


def englishToPigLatin(message):
    pigLatin = ''  # # Łańcuch znaków z wiadomością przetłumaczoną na świńską łacinę
    for word in message.split():
        # Oddziel znaki znajdujące się na początku słowa, które nie są literami:
        prefixNonLetters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefixNonLetters += word[0]
            word = word[1:]
        if len(word) == 0:
            pigLatin = pigLatin + prefixNonLetters + ' '
            continue

        # Oddziel znaki znajdujące się na końcu słowa, które nie są literami:
        suffixNonLetters = ''
        while not word[-1].isalpha():
            suffixNonLetters = word[-1] + suffixNonLetters
            word = word[:-1]

        # Zapamiętaj, czy słowo było zapisane wielką literą lub czy było nazwą własną.
        wasUpper = word.isupper()
        wasTitle = word.istitle()

        word = word.lower()  # Zmień litery słowa na małe na potrzeby tłumaczenia.

        # Oddziel spółgłoski znajdujące się na początku słowa:
        prefixConsonants = ''
        while len(word) > 0 and not word[0] in VOWELS:
            prefixConsonants += word[0]
            word = word[1:]

        # Dodaj końcówkę świńskiej łaciny:
        if prefixConsonants != '':
            word += prefixConsonants + 'aj'
        else:
            word += 'jaj'

        # Przywróć wielkie litery w słowie lub zamień z powrotem na nazwę własną:
        if wasUpper:
            word = word.upper()
        if wasTitle:
            word = word.title()

        # Z powrotem dodaj znaki niebędące literami na początku lub na końcu słowa.
        pigLatin += prefixNonLetters + word + suffixNonLetters + ' '
    return pigLatin


if __name__ == '__main__':
    main()
