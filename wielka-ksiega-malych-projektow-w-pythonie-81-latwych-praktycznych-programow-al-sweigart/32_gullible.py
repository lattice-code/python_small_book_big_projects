"""Naiwniak, autor: Al Sweigart, al@inventwithpython.com
Jak znaleźć zajęcia na wiele godzin dla osoby łatwowiernej. (To program-żart.)
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, dla początkujących, zabawny"""

print('Naiwniak, autor: Al Sweigart, al@inventwithpython.com')

while True:  # Główna pętla programu.
    print('Chcesz znaleźć zajęcie na wiele godzin dla osoby łatwowiernej? T/N')
    response = input('> ')  # Pobierz odpowiedź gracza.
    if response.lower() == 'nie' or response.lower() == 'n':
        break  # Jeśli "nie", wyjdź z pętli.
    if response.lower() == 'tak' or response.lower() == 't':
        continue  # Jeśli "tak", wykonuj dalej tę pętlę, wracając do początku.
    print('"{}" nie jest odpowiedzią typu tak/nie.'.format(response))

print('Dziękujemy. Życzymy miłego dnia!')
