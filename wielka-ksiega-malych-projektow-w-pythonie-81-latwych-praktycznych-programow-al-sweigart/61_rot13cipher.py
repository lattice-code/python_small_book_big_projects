"""Szyfr ROT13, autor: Al Sweigart, al@inventwithpython.com
Najprostszy szyfr przesuwający do szyfrowania i odszyfrowywania tekstu.
Więcej informacji na stronie https://pl.wikipedia.org/wiki/ROT13.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, kryptografia"""

try:
    import pyperclip  # Moduł pyperclip kopiuje tekst do schowka.
except ImportError:
    pass  # Jeśli moduł pyperclip nie jest zainstalowany, nic się nie dzieje. Jego brak nie stanowi problemu.

# Deklaracja stałych:
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

print('Szyfr ROT13, autor: Al Sweigart, al@inventwithpython.com')
print()

while True:  # Główna pętla programu.
    print('Wpisz wiadomość do zaszyfrowania/odszyfrowania (lub KONIEC):')
    message = input('> ')

    if message.upper() == 'KONIEC':
        break  # Wyjdź z głównej pętli programu.

    # Przesuń litery w wiadomości o 13 miejsc:
    translated = ''
    for character in message:
        if character.isupper():
            # Dołącz przetłumaczone wielkie litery:
            transCharIndex = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[transCharIndex]
        elif character.islower():
            # Dołącz przetłumaczone małe litery:
            transCharIndex = (LOWER_LETTERS.find(character) + 13) % 26
            translated += LOWER_LETTERS[transCharIndex]
        else:
            # Dołącz nieprzetłumaczone znaki:
            translated += character

    # Wyświetl tłumaczenie:
    print('Przetłumaczona wiadomość to:')
    print(translated)
    print()

    try:
        # Skopiuj tłumaczenie do schowka:
        pyperclip.copy(translated)
        print('(Skopiowano do schowka.)')
    except:
        pass
