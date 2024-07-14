"""Generator kalendarza, autor: Al Sweigart, al@inventwithpython.com
Tworzy kartkę z kalendarza na dany miesiąc, zapisuje w pliku tekstowym i przygotowuje do druku.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki"""

import datetime

# Deklaracja stałych:
DAYS = ('Niedziela', 'Poniedziałek', 'Wtorek', 'Środa', 'Czwartek',
        'Piątek', 'Sobota')
MONTHS = ('Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec',
          'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień')

print('Generator kalendarza, autor: Al Sweigart, al@inventwithpython.com')

while True:  # Pętla pytająca użytkownika o rok.
    print('Podaj rok dla kalendarza:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Podaj rok jako wartość liczbową, na przykład 2023.')
    continue

while True:  # Pętla pytająca użytkownika o miesiąc.
    print('Podaj miesiąc dla kalendarza, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Podaj miesiąc jako liczbę, na przykład 3 dla marca.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Podaj liczbę od 1 do 12.')


def getCalendarFor(year, month):
    calText = ''  # Zmienna calText będzie przechowywać łańcuch znaków dla naszego kalendarza.

    # Miesiąc i rok umieść na górze kalendarza:
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # Dodaj do kalendarza oznaczenia dni tygodnia.
    # (!) Spróbuj zamienić pełne nazwy na skróty: NIE, PON, WTO itd.
    calText += '.Niedziela.Poniedziałek..Wtorek.....Środa.....Czwartek.....Piątek....Sobota..\n'

    # Linia pozioma rozdzielająca tygodnie:
    weekSeparator = ('+----------' * 7) + '+\n'

    # Puste wiersze mają 10 spacji między separatorami dni, |:
    blankRow = ('|          ' * 7) + '|\n'

    # Znajdź pierwszą datę w miesiącu. (Moduł datetime obsługuje wszystkie
    # skomplikowane zadania związane z datami).
    currentDate = datetime.date(year, month, 1)

    # Cofaj currentDate, dopóki nie będzie to niedziela. (Funkcja weekday() zwraca
    # dla niedzieli 6, nie 0).
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:  # Pętla przechodzi przez każdy tydzień w miesiącu.
        calText += weekSeparator

        # Zmienna dayNumberRow jest wierszem z numerami dni:
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) # Przejdź do następnego dnia.
        dayNumberRow += '|\n'  # Dodaj pionową linię po sobocie.

        # Do tekstu kalendarza dodaj wiersz z numerami dni i 3 puste wiersze.
        calText += dayNumberRow
        for i in range(3):  # (!) Spróbuj zmienić tę wartość z 3 na 5 lub 10.
            calText += blankRow

        # Sprawdź, czy wszystkie dni miesiąca zostały uwzględnione:
        if currentDate.month != month:
            break

    # Dodaj linię poziomą na samym dole kalendarza.
    calText += weekSeparator
    return calText


calText = getCalendarFor(year, month)
print(calText)  # Wyświetl kalendarz.

# Zapisz kalendarz w pliku tekstowym:
calendarFilename = 'kalendarz{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print('Zapisano z nazwą ' + calendarFilename)
