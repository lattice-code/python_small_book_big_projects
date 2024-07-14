"""Podchwytliwe pytania, autor: Al Sweigart, al@inventwithpython.com
Quiz z podchwytliwymi pytaniami.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety:  długi, zabawny"""

import random, sys

# QUESTIONS to lista słowników. Każdy słownik to pytanie i odpowiedź na nie.
# Słownik ma klucze: 'question' (przechowuje pytanie),
#  'answer' (przechowuje odpowiedź)
# oraz 'accept' (przechowuje listę łańcuchów znaków,
# które są akceptowane jako poprawna odpowiedź).
# (!) Spróbuj dodać tutaj własne podchwytliwe pytania:
QUESTIONS = [
 {'question': "Ile razy możesz wziąć 2 jabłka ze stosu 10 jabłek?",
  'answer': "Jeden raz. Potem jest już tylko stos 8 jabłek.",
  'accept': ['jeden raz', 'raz', 'jeden' '1']},
 {'question': "Czy można narysować kwadrat z trzema bokami?",
  'answer': "Tak. Wszystkie kwadraty mają trzy boki. Mają również czwarty bok.",
  'accept': ['tak']},
 {'question': "Ile razy można złożyć na pół kartkę papieru bez odginania?",
  'answer': "Raz. Potem będziesz składał już na ćwiartki.",
  'accept': ['raz', '1', 'jeden raz', 'jeden']},
 {'question': "Jaki jest ręcznik, kiedy wysycha?",
  'answer': "Mokry.",
  'accept': ['mokry']},
 {'question': "Jaki staje się ręcznik, gdy wysycha?",
  'answer': "Suchszy.",
  'accept': ['suchszy', 'suchy']},
 {'question': "Wyobraź sobie, że jesteś w nawiedzonym domu pełnym złych duchów. Co musisz zrobić, by być bezpieczny?",
  'answer': "Nic. Ponieważ tylko to sobie wyobrażasz.",
  'accept': ['nic', 'przestać']},
{'question': "Kierowca taksówki porusza się pod prąd drogą jednokierunkową. Mija policję, ale nie dostaje mandatu. Dlaczego?",
  'answer': "Idzie.",
  'accept': ['idzie']},
 {'question': "Jaki będzie żółty kamień wrzucony do niebieskiego stawu?",
  'answer': "Mokry.",
  'accept': ['mokry']},
 {'question': "Ile kilometrów musi przejechać rowerzysta, by dostać się na trening?",
  'answer': "Zero. Zaczyna trening, jak tylko wsiądzie na rower.",
  'accept': ['nic', 'zero', '0']},
 {'question': "Z jakiego budynku ludzie chcą wyjść zaraz po wejściu do niego?",
  'answer': "Lotnisko.",
  'accept': ['lotnisko', 'autobus', 'port', 'pociąg', 'stacja', 'przystanek']},
 {'question': "Jeśli jesteś na środku kwadratu domu, patrzysz na zachód, południe masz po swojej lewej, a północ po prawej, to obok której ściany domu stoisz?",
  'answer': "Żadnej. Stoisz pośrodku.",
  'accept': ['żadnej', 'środek', 'w środku', 'każdej']},
 {'question': "Ile ziemi jest w dziurze 3 metry szerokiej, 3 metry długiej i 3 metry głębokiej?",
  'answer': "W dziurze nie ma ziemi.",
  'accept': ['nie ma', 'nic', 'zero']},
 {'question': "Dziewczyna wysyła list z Ameryki do Japonii. O ile mil przesunął się znaczek?",
  'answer': "Zero. Znaczek był cały czas w tym samym miejscu na kopercie.",
  'accept': ['zero', '0', 'nic']},
 {'question': "Która góra była najwyższa na Ziemi przed odkryciem  Mount Everest?",
  'answer': "Mount Everest zawsze był najwyższą górą na Ziemi, mimo że nie był jeszcze odkryty.",
  'accept': ['everest']},
 {'question': "Ile palców większość ludzi ma w obu dłoniach?",
  'answer': "Osiem. Mają również dwa kciuki.",
  'accept': ['osiem', '8']},
 {'question': "W Polsce 11 listopada jest dniem wolnym. Czy w Anglii mają 11 listopada?",
  'answer': "Tak. Wszystkie kraje mają 11 listopada w swoich kalendarzach.",
  'accept': ['tak']}, 
 {'question': "Jak lekarz może wytrzymać 30 dni bez snu?",
  'answer': "Dzięki spaniu w nocy.",
  'accept': ['noc', 'spanie']},
 {'question': "Ile miesięcy ma 28 dni?",
  'answer': "12. Wszystkie miesiące mają 28 dni. Niektóre z nich mają więcej.",
  'accept': ['12', 'dwanaście', 'wszystkie']},
 {'question': "Ile dwukilowych cegieł jest w tuzinie?",
  'answer': "Tuzin.",
  'accept': ['12', 'dwanaście', 'tuzin']},
 {'question': "Dlaczego pochowanie w Dakocie Południowej osoby żyjącej w Dakocie Północnej jest nielegalne?",
  'answer': "Ponieważ nie można pochować nikogo żywcem.",
  'accept': ['żyje', 'żywy', 'żyjący']},
 {'question': "Jaki pojazd ma cztery koła i muchy?",
  'answer': "Śmieciarka.",
  'accept': ['śmieciarka', 'śmieci']},
 {'question': "Jaki pojazd ma cztery koła i lata?",
  'answer': "Samolot.",
  'accept': ['samolot', 'aeroplan']},
 {'question': "Mama Gosi ma pięć córek. Cztery z nich mają na imię Haha, Hehe, Hihi i Hoho. Jak ma na imię piąta córka?",
  'answer': "Gosia.",
  'accept': ['gosia']},
 {'question': "Jak długie jest ogrodzenie, jeśli są w nim trzy słupki oddalone od siebie o metr?",
  'answer': "Dwa metry.",
  'accept': ['2', 'dwa']},
 {'question': "Ile nóg ma pies, jeśli nazwiesz jego ogon nogą?",
  'answer': "Cztery. Nazywanie ogona nogą nie sprawi, że nią będzie.",
  'accept': ['cztery', '4']},
 {'question': "Ile warte jest 1976 groszy w porównaniu z 1975 groszami?",
  'answer': "Jeden grosz.",
  'accept': ['1', 'jeden']},
 {'question': "Jakich dwóch posiłków nigdy nie zjesz na śniadanie?",
  'answer': "Obiadu i kolacji.",
  'accept': ['obiad', 'kolacja', 'lunch']},
 {'question': "Ile dni urodzin ma przeciętna osoba?",
  'answer': "Jeden. Rodzisz się tylko raz.",
  'accept': ['jeden', '1', 'raz' 'narodziny']},
 {'question': "Gdzie została podpisana Deklaracja Praw Człowieka?",
  'answer': "Na dole.",
  'accept': ['na dole']},
 {'question': "Ktoś wkłada dwa orzechy do swojej kieszeni, ale pięć minut później w jego kieszeni jest tylko jedna rzecz. Co to jest?",
  'answer': "Dziura.",
  'accept': ['dziura']},
 {'question': "Co takiego tworzy rzeźbiarz, czego nikt nie może zobaczyć?",
  'answer': "Hałas.",
  'accept': ['hałas']},
 {'question': "Czy gdy upuścisz surowe jajko na betonową podłogę, to się rozbije?",
  'answer': "Nie. Betonową podłogę trudno rozbić.",
  'accept': ['nie']},
 {'question': "Jeśli dziesięciu ludzi potrzebowało dziesięciu godzin, by wybudować mur, ilu godzin potrzebuje pięciu ludzi, by go wybudować?",
  'answer': "Zero. Jest już wybudowany.",
  'accept': ['zero', 'nic', '0', 'już', 'wybudowany']},
 {'question': "Co jest cięższe, 100 kilo kamieni czy 100 kilo pierza?",
  'answer': "Żadna z tych rzeczy. Ważą tyle samo.",
  'accept': ['żadna', 'nic', 'nie', 'tyle samo', 'równie', 'równowaga']},
 {'question': "Co musisz zrobić, by przeżyć ugryzienie zatrutego węża?",
  'answer': "Nic. Tylko jadowite węże są zabójcze.",
  'accept': ['nic']},
 {'question': "Jake mamy trzy następujące po sobie dni, gdy żaden z nich nie jest niedzielą, środą ani piątkiem?",
  'answer': "Wczoraj, dzisiaj i jutro.",
  'accept': ['wczoraj', 'dzisiaj', 'jutro']},
 {'question': "Jest dziesięć jabłek. Zabrałeś dwa. Ile jabłek Ci zostało?",
  'answer': "Dwa.",
  'accept': ['2', 'dwa']},
 {'question': "39-letni mężczyzna urodził się 22 lutego. W którym roku wypadają jego urodziny?",
  'answer': "Jego urodziny są co roku 22 lutego.",
  'accept': ['każdy', 'co roku']},
 {'question': "Jak daleko możesz wejść w las?",
  'answer': "Pół drogi. Potem zaczynasz już wychodzić z lasu.",
  'accept': ['połowa', '1/2']},
 {'question': "Czy mężczyzna może poślubić siostrę swojej owdowiałej żony?",
  'answer': "Nie, bo jest martwy.",
  'accept': ['nie']},
 {'question': "Co otrzymasz, gdy podzielisz sto przez pół?",
  'answer': "Sto podzielone przez pół to dwieście. Sto podzielone na pół to pięćdziesiąt.",
  'accept': ['dwieście', '200']},
 {'question': "Jak nazywamy kogoś, kto zawsze wie, gdzie jest jego małżonek lub małżonka?",
  'answer': "Wdowiec lub wdowa.",
  'accept': ['wdowa', 'wdowiec']},
 {'question': "Pociąg elektryczny odjeżdża ze stacji Warszawa o 16 w poniedziałek i udaje się na południe z prędkością 100 kilometrów na godzinę. W którą stronę leci dym z komina?",
  'answer': "Pociągi elektryczne nie mają kominów.",
  'accept': ["w żadną", "nie", 'w ogóle']},
 {'question': "Kto pełni funkcję prezedenta Stanów Zjednoczonych, gdy wiceprezedent umiera?",
  'answer': "Obecny prezydent Stanów Zjednoczonych.",
  'accept': ['prezydent', 'aktualny', 'obecny']},
 {'question': "Lekarz przepisuje Ci trzy tabletki i zaleca brać jedną co pół godziny. Na jak długo starczą Ci tabletki?",
  'answer': "Na godzinę.",
  'accept': ['1', 'na godzinę', 'jedna']},
 {'question': "Gdzie jest ocean bez wody?",
  'answer': "Na mapie.",
  'accept': ['mapa']},
 {'question': "Co jest tak duże jak nosorożec, ale nic nie waży?",
  'answer': "Cień nosorożca.",
  'accept': ['cień']},
 {'question': "Sprzedawca w sklepie mięsnym ma dokładnie 177 centymetrów wzrostu, a waży?",
  'answer': "Sprzedawca waży mięso.",
  'accept': ['mięso']}]

CORRECT_TEXT = ['Dobrze!', 'Poprawna odpowiedź.', "Masz rację.",
                    'Super.', 'Gratulacje!']
INCORRECT_TEXT = ['Źle!', "Nie, to nie o to chodzi.", 'Nie.',
                      'Nie do końca.', 'Zła odpowiedź.']

print('''Podchwytliwe pytania, autor: Al Sweigart, al@inventwithpython.com

Czy znasz odpowiedzi na te podchwytliwe pytania?
(Wpisz KONIEC, by wyjść z gry.)
''')

input('Naciśnij Enter, aby rozpocząć...')

random.shuffle(QUESTIONS)
score = 0

for questionNumber, qa in enumerate(QUESTIONS):  # Główna pętla programu.
    print('\n' * 40)  # "Wyczyść" ekran.
    print('Pytanie:', questionNumber + 1)
    print('Wynik:', score, '/', len(QUESTIONS))
    print('PYTANIE:', qa['question'])
    response = input('  ODPOWIEDŹ: ').lower()

    if response == 'koniec':
        print('Dziękujemy za grę!')
        sys.exit()

    correct = False
    for acceptanceWord in qa['accept']:
        if acceptanceWord in response:
            correct = True

    if correct:
        text = random.choice(CORRECT_TEXT)
        print(text, qa['answer'])
        score += 1
    else:
        text = random.choice(INCORRECT_TEXT)
        print(text, 'Odpowiedź brzmi:', qa['answer'])
    response = input('Naciśnij Enter, by zobaczyć następne pytanie...').lower()

    if response == 'quit':
        print('Dziękujemy za grę!')
        sys.exit()

print('To już wszystkie pytania. Dziękujemy za grę!')
