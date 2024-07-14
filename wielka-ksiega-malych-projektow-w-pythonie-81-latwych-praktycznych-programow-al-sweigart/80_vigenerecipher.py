"""Szyfr Vigenère'a, autor: Al Sweigart, al@inventwithpython.com
Szyfr Vigenère'a to  wieloliterowy szyfr podstawieniowy,
tak silny, że przez setki lat nikt nie potrafił go złamać.
Więcej informacji na stronie:https://pl.wikipedia.org/wiki/Szyfr_Vigen%C3%A8re%E2%80%99a.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, kryptografia, matematyka"""

try:
    import pyperclip  # Moduł pyperclip kopiuje tekst do schowka.
except ImportError:
    pass  # Jeśli moduł pyperclip nie jest zainstalowany, nic nie rób. To nie stanowi problemu.

# Każdy możliwy znak, który może być zaszyfrowany i odszyfrowany:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    print('''Szyfr Vigenère'a, autor: Al Sweigart, al@inventwithpython.com
Szyfr Vigenère'a to  wieloliterowy szyfr podstawieniowy,
tak silny, że przez setki lat nikt nie mógł go złamać.''')

    # Spytaj użytkownika, czy chce zaszyfrować, czy odszyfrować tekst:
    while True:  # Pytaj dopóki, użytkownik nie odpowie z lub o.
        print('Czy chcesz (z)aszyfrować, czy (o)dszyfrować tekst?')
        response = input('> ').lower()
        if response.startswith('z'):
            myMode = 'zaszyfrowan'
            break
        elif response.startswith('o'):
            myMode = 'odszyfrowan'
            break
        print('Proszę, wpisz literę z lub o.')

    # Poproś użytkownika o podanie klucza:
    while True:  # Pytaj, dopóki użytkownik nie poda odpowiedniego klucza.
        print('Proszę, podaj klucz.')
        print('Może to być słowo lub dowolna kombinacja liter:')
        response = input('> ').upper()
        if response.isalpha():
            myKey = response
            break

    # Poproś użytkownika o wpisanie wiadomości do zaszyfrowania/odszyfrowania:
    print('Wpisz wiadomość do {}ia.'.format(myMode))
    myMessage = input('> ')

    # Zaszyfruj/odszyfruj wiadomość:
    if myMode == 'zaszyfrowan':
        translated = encryptMessage(myMessage, myKey)
    elif myMode == 'odszyfrowan':
        translated = decryptMessage(myMessage, myKey)

    print('%sa wiadomość:' % (myMode.title()))
    print(translated)

    try:
        pyperclip.copy(translated)
        print('Cały %sy tekst został skopiowany do schowka.' % (myMode))
    except:
        pass  # Nic nie rób, jeśli moduł pyperclip nie został zainstalowany.


def encryptMessage(message, key):
    """Szyfruje wiadomość za pomocą podanego klucza."""
    return translateMessage(message, key, 'zaszyfrowan')


def decryptMessage(message, key):
    """Odszyfrowuje wiadomość za pomocą podanego klucza."""
    return translateMessage(message, key, 'odszyfrowan')


def translateMessage(message, key, mode):
    """Szyfruje lub odszyfrowuje wiadomość za pomocą podanego klucza."""
    translated = []  # Przechowuje zaszyfrowany/odszyfrowany łańcuch znaków.

    keyIndex = 0
    key = key.upper()

    for symbol in message:  # Przejdź w pętli przez każdy znak wiadomości.
        num = LETTERS.find(symbol.upper())
        if num != -1:  # -1 oznacza, że znak symbol.upper() nie występuje w liście LETTERS.
            if mode == 'zaszyfrowan':
                # Dodaj po zaszyfrowaniu:
                num += LETTERS.find(key[keyIndex])
            elif mode == 'odszyfrowan':
                # Odejmij po odszyfrowaniu:
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS)  # Obsłuż potencjalne zawinięcie tekstu.

            # Dodaj zaszyfrowany/odszyfrowany znak do listy przetłumaczonych znaków.
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1  # Przejdź do następnej litery klucza.
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # Po prostu dodaj symbol bez szyfrowania/odszyfrowywania:
            translated.append(symbol)

    return ''.join(translated)


# Jeżeli ten program został uruchomiony (a nie zaimportowany), uruchom program:
if __name__ == '__main__':
    main()
