"""Moduł sevseg, autor: Al Sweigart, al@inventwithpython.com
Moduł wyświetlający liczby w stylu wyświetlacza siedmiosegmentowego, wykorzystany
w programach Odliczanie i Zegar cyfrowy.
Więcej informacji na stronie https://pl.wikipedia.org/wiki/Wy%C5%9Bwietlacz_siedmiosegmentowy.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, moduł"""

"""Wyświetlacz siedmiosegmentowy z oznaczeniami, każdy segment oznaczony literami od A do G:
 __A__
|     |    Każda cyfra wyświetlacza siedmiosegmentowego:
F     B     __       __   __        __   __  __   __   __
|__G__|    |  |   |  __|  __| |__| |__  |__    | |__| |__|
|     |    |__|   | |__   __|    |  __| |__|   | |__|  __|
E     C
|__D__|"""


def getSevSegStr(number, minWidth=0):
    """Zwraca łańcuch znaków liczby wstylu wyświetlacza siedmiosegmentowego. Przed zwróconym
    łańcuchem znaków zostaną umieszczone zera, jeśli liczba ma mniej cyfr niż wartość minimalna minWidth."""

    # Zamień liczbę na łańcuch znaków, gdy ta jest typu int (całkowita) lub float (zmiennoprzecinkowa):
    number = str(number).zfill(minWidth)

    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == '.':  # Wyświetl znak dziesiętny.
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue  # Pomiń odstęp między cyframi.
        elif numeral == '-':  # Wyświetl znak minusa:
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0':  # Wyświetl 0.
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':  # Wyświetl 1.
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2':  # Wyświetl 2.
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == '3':  # Wyświetl 3.
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4':  # Wyświetl 4.
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':  # Wyświetl 5.
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == '6':  # Wyświetl 6.
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numeral == '7':  # Wyświetl 7.
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8':  # Wyświetl 8.
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':  # Wyświetl 9.
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'

        # Dodaj spację (dla odstępów między liczbami), 
        # jeśli to nie jest ostatnia cyfra, a znak dziesiętny nie jest następny:
        if i != len(number) - 1 and number[i + 1] != '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '

    return '\n'.join(rows)


# Jeśli ten program nie jest importowany, wyświetl liczby od 00 do 99.
if __name__ == '__main__':
    print('Ten moduł jest przeznaczony bardziej do importowania niż do uruchamiania bezpośrednio.')
    print('Na przykład ten kod:')
    print('    import sevseg')
    print('    myNumber = sevseg.getSevSegStr(42, 3)')
    print('    print(myNumber)')
    print()
    print('...wyświetli 42, z zerem na początku, by liczba była trzycyfrowa:')
    print(' __        __ ')
    print('|  | |__|  __|')
    print('|__|    | |__ ')
