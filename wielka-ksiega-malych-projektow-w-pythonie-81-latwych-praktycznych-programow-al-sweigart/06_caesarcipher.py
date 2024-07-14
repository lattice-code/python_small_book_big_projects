"""Szyfr Cezara, autor: Al Sweigart, al@inventwithpython.com
Szyfr Cezara jest szyfrem przesuwającym, który używa dodawania i odejmowania,
by szyfrować i odszyfrowywać litery.
Więcej informacji: https://pl.wikipedia.org/wiki/Szyfr_Cezara.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, dla początkujących, kryptografia, matematyka"""

try:
    import pyperclip  # Biblioteka pyperclip kopiuje tekst do schowka.
except ImportError:
    pass  # Jeśli biblioteka pyperclip nie jest zainstalowana, nic nie rób. To nie jest duży problem.

# Każdy  znak, który może być zaszyfrowany/odszyfrowany:
# (!) Możesz dodać liczby i znaki interpunkcyjne,
# by również je móc szyfrować.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Szyfr Cezara, autor: Al Sweigart, al@inventwithpython.com')
print('Szyfr Cezara szyfruje litery przez przesunięcie ich o liczbę,')
print('która jest kluczem. Na przykład klucz 2 oznacza, że litera A jest')
print('zamieniona na C, litera B na D i tak dalej.')
print()

# Użytkownik decyduje, czy chce zaszyfrować, czy odszyfrować wiadomość:
while True:  # Pytaj, dopóki użytkownik nie poda z lub o.
    print('Czy chcesz (z)aszyfrować, czy (o)dszyfrować?')
    response = input('> ').lower()
    if response.startswith('z'):
        mode = 'zaszyfrowania'
        break
    elif response.startswith('o'):
        mode = 'odszyfrowania'
        break
    print('Proszę podać literę z lub o.')

# Użytkownik ustala klucz:
while True:  # Pytaj dopóki użytkownik nie poda odpowiedniego klucza.
    maxKey = len(SYMBOLS) - 1
    print('Proszę podać klucz (0 do {}).'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# Użytkownik podaje wiadomość do zaszyfrowania/odszyfrowania:
print('Wpisz wiadomość do {}.'.format(mode))
message = input('> ')

# Szyfr Cezara działa tylko na wielkich literach:
message = message.upper()

# Zapisz zaszyfrowaną/odszyfrowaną wersję wiadomości:
translated = ''

# Zaszyfruj/odszyfruj każdą literę w wiadomości:
for symbol in message:
    if symbol in SYMBOLS:
        # Znajdź zaszyfrowany (lub odszyfrowany) numer dla tego symbolu.
        num = SYMBOLS.find(symbol)  # Znajdź numer dla tego symbolu.
        if mode == 'zaszyfrowania':
            num = num + key
        elif mode == 'odszyfrowania':
            num = num - key

        # Obsługa zawijania numeracji, gdy numer symbolu jest większy
        # niż długość łańcucha znaków SYMBOLS lub mniejszy niż 0:
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # Dodaj zaszyfrowany/odszyfrowany numer symbolu do zmiennej translated:
        translated = translated + SYMBOLS[num]
    else:
        # Po prostu dodaj symbol bez szyfrowania/odszyfrowywania:
        translated = translated + symbol

# Wyświetl na ekranie zaszyfrowany/odszyfrowany łańcuch znaków:
print(translated)

try:
    pyperclip.copy(translated)
    print('Tekst przekazany do {} został skopiowany do schowka.'.format(mode))
except:
    pass  # Nic nie rób, jeśli biblioteka pyperclip nie została zainstalowana.
