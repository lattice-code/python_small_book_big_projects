"""Układ okresowy pierwiastków, autor: Al Sweigart, al@inventwithpython.com
Wyświetla informacje o wszystkich pierwiastkach.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: krótki, nauka"""

# Dane pochodzą ze strony https://en.wikipedia.org/wiki/List_of_chemical_elements.
# Zaznacz tabelę, skopiuj ją, a następnie wklej do arkusza kalkulacyjnego,
# na przykład Excel lub Google Sheets. Przykładem jest plik: https://invpy.com/elements.
# Następnie zapisz ten plik jako periodictable.csv.
# Lub pobierz ten plik csv z: https://invpy.com/periodictable.csv.

import csv, sys, re

# Wczytaj wszystkie dane z pliku periodictable.csv.
elementsFile = open('periodictable.csv', encoding='utf-8')
elementsCsvReader = csv.reader(elementsFile)
elements = list(elementsCsvReader)
elementsFile.close()

ALL_COLUMNS = ['Liczba atomowa', 'Symbol', 'Pierwiastek', 'Etymologia nazwy',
               'Grupa', 'Okres', 'Masa atomowa', 'Gęstość',
               'Temperatura topnienia', 'Temperatura wrzenia',
               'Pojemność cieplna', 'Elektroujemność',
               'Występowanie na Ziemi']

# W celu wyrównania tekstu musimy znaleźć najdłuższy łańcuch znaków w liście ALL_COLUMNS.
LONGEST_COLUMN = 0
for key in ALL_COLUMNS:
    if len(key) > LONGEST_COLUMN:
        LONGEST_COLUMN = len(key)

# Umieść wszystkie dane pierwiastków w strukturze danych:
ELEMENTS = {}  # Struktura danych, w której zapisane są wszystkie dane pierwiastka.
for line in elements:
    element = {'Liczba atomowa':  line[0],
               'Symbol':         line[1],
               'Pierwiastek':        line[2],
               'Etymologia nazwy': line[3],
               'Grupa':          line[4],
               'Okres':         line[5],
               'Masa atomowa':  line[6] + ' u', # jednostka masy atmowej
               'Gęstość':        line[7] + ' g/cm^3', # gramy/centymetry sześcienne
               'Temperatura topnienia':  line[8] + ' K', # kelwin
               'Temperatura wrzenia':  line[9] + ' K', # kelwin
               'Pojemność cieplna':      line[10] + ' J/(g*K)',
               'Elektroujemność':           line[11],
               'Występowanie na Ziemi': line[12] + ' mg/kg'}

    # Niektóre dane mają w nawiasach kwadratowych tekst, który chcemy usunąć,
    # na przykład masa atomowa boru:
    # "10.81[III][IV][V][VI]" powinno być "10.81"

    for key, value in element.items():
        # Usuń tekst - [liczba rzymska]:
        element[key] = re.sub(r'\[(I|V|X)+\]', '', value)

    ELEMENTS[line[0]] = element  # Przypisz liczbę atomową do pierwiastka.
    ELEMENTS[line[1]] = element  # Przypisz symbol do pierwiastka.

print('Układ okresowy pierwiastków')
print('autor: Al Sweigart, al@inventwithpython.com')
print()

while True:  # Główna pętla programu.
    # Pokaż tabelę i pozwól użytkownikowi wybrać pierwiastek:
    print('''            Układ okresowy pierwiastków
      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
    1 H                                                  He
    2 Li Be                               B  C  N  O  F  Ne
    3 Na Mg                               Al Si P  S  Cl Ar
    4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

            Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
            Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')
    print('Podaj symbol lub liczbę atomową, by uzyskać więcej informacji na temat danego pierwiastka, albo KONIEC, by wyjść z programu.')
    response = input('> ').title()

    if response == 'Koniec':
        sys.exit()

    # Wyświetl dane wybranego pierwiastka:
    if response in ELEMENTS:
        for key in ALL_COLUMNS:
            keyJustified = key.rjust(LONGEST_COLUMN)
            print(keyJustified + ': ' + ELEMENTS[response][key])
        input('Naciśnij Enter, aby kontynuować...')
