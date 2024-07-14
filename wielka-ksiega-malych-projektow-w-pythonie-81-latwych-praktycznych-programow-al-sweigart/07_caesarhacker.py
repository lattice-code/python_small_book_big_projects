"""Łamacz szyfru Cezara, autor: Al Sweigart, al@inventwithpython.com
Ten program odtajnia wiadomości zaszfrowane przy użyciu szyfru Cezara
za pomocą ataku brute force sprawdzającego każdy możliwy klucz.
Więcej informacji na stronie
https://pl.wikipedia.org/wiki/Szyfr_Cezara#Kryptoanaliza.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, dla początkujących, kryptografia, matematyka"""

print('Łamacz szyfru Cezara, autor: Al Sweigart, al@inventwithpython.com')

# Użytkownik podaje wiadomość do odszyfrowania:
print('Wpisz wiadomość zaszyfrowaną szyfrem Cezara, którą chcesz odtajnić.')
message = input('> ')

# Każdy  znak, który może być zaszyfrowany/odszyfrowany:
# (Łańcuch znaków SYMBOLS musi być taki sam jak podczas szyfrowania wiadomości).
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):  # Sprawdź za pomocą pętli każdy możliwy klucz.
    translated = ''

    # Odszyfruj każdy symbol w wiadomości:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)  # Znajdź numer symbolu.
            num = num - key  # Odszyfruj numer.

            # Obsługa zawijania numeracji, gdy numer symbolu jest mniejszy od zera.
            if num < 0:
                num = num + len(SYMBOLS)

            # Dodaj odszyfrowany numer symbolu do zmiennej translated:
            translated = translated + SYMBOLS[num]
        else:
            # Po prostu dodaj symbol bez odszyfrowywania:
            translated = translated + symbol

    # Wyświetl na ekranie klucz wraz z odszyfrowanym tekstem:
    print('Klucz #{}: {}'.format(key, translated))
