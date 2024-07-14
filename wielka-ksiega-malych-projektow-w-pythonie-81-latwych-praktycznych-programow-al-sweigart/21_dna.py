"""DNA, autor: Al Sweigart, al@inventwithpython.com
Prosta animacja podwójnej helisy DNA. Naciśnij Ctrl+C, by zatrzymać program.
Program zainspirowany projektem matokena: https://asciinema.org/a/155441.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, artystyczny, przewijanie, nauka"""

import random, sys, time

PAUSE = 0.15  # (!) Spróbuj zmienić tę wartość na 0.5 lub 0.0.

# To są pojednyncze wiersze animacji DNA:
ROWS = [
    #123456789 <- Użyj tego do zmierzenia liczby spacji:
    '         ##',  # Indeks 0 nie ma {}.
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',  # Indeks 9 nie ma {}.
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']
    # 123456789 <- Użyj tego do zmierzenia liczby spacji:

try:
    print('Animacja DNA, autor: Al Sweigart, al@inventwithpython.com')
    print('Naciśnij Ctrl+C, by wyjść...')
    time.sleep(2)
    rowIndex = 0

    while True:  # Główna pętla programu.
        # Zwiększ zmienną rowIndex, by narysować następny wiersz:
        rowIndex = rowIndex + 1
        if rowIndex == len(ROWS):
            rowIndex = 0

        # Wiersze o indeksach 0 i 9 nie mają nukleotydów:
        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue

        # Wybierz losowe pary nukleotydów, guanina-cytozyna oraz
        # adenina-tymina:
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = 'A', 'T'
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = 'T', 'A'
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = 'C', 'G'
        elif randomSelection == 4:
            leftNucleotide, rightNucleotide = 'G', 'C'

        # Wyświetl wiersz.
        print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(PAUSE)  # Dodaj krótką pauzę.
except KeyboardInterrupt:
    sys.exit()  # Po naciśnięciu Ctrl+C zakończ program.
