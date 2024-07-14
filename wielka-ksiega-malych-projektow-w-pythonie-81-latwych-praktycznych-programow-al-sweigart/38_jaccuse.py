"""OSKARŻAM!, autor: Al Sweigart, al@inventwithpython.com
Gra detektywistyczna o zagubionym kocie.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: bardzo długi, gra, zabawny, łamigłówka"""

# Zagraj w oryginalną grę stworzoną we Flashu na stronie
# https://homestarrunner.com/videlectrix/wheresanegg.html.
# Więcej informacji (w języku angielskim) na stronie http://www.hrwiki.org/wiki/Where's_an_Egg%3F.

import time, random, sys

# Deklaracja stałych:
SUSPECTS = ['HRABIA HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR', 'PANI FEATHERTOSS', 'DR JEAN SPLICER', 'KLAUN RAFFLES', 'ESPRESSA TOFFEEPOT', 'CECIL EDGAR VANDERTON']
ITEMS = ['LATARKA', 'ŚWIECZNIK', 'TĘCZOWA FLAGA', 'KARUZELA CHOMIKA', 'KASETA VHS Z ANIME', 'SŁOIK OGÓRKÓW', 'JEDEN KOWBOJSKI BUT', 'CZYSTE MAJTKI', 'KARTA PODARUNKOWA']
PLACES = ['ZOO', 'STARA STODOŁA', 'JEZIORO Z KACZKAMI', 'RATUSZ', 'POPULARNA KAWIARNIA', 'DYSKOTEKA', 'MUZEUM GIER WIDEO', 'BIBLIOTEKA UNIWERSYTECKA', 'AKWEN Z ALIGATOREM ALBINOSEM']
TIME_TO_SOLVE = 300  # 300 sekund (5 minut) na rozwiązanie zagadki.

# Pierwsze litery i najdłuższa nazwa miejsca są potrzebne do wyświetlania menu:
PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)

# Podstawowe sprawdzenie, czy jest tyle samo miejsc, podejrzanych i przedmiotów:
assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9
# Pierwsze litery muszą być unikatowe:
assert len(PLACE_FIRST_LETTERS.keys()) == len(PLACES)


knownSuspectsAndItems = []
# Słownik odwiedzonych miejsc (visitedPlaces), gdzie kluczami są miejsca, a  wartościami podejrzani i przedmioty, które tam się znajdują.
visitedPlaces = {}
currentLocation = 'TAXI'  # Rozpocznij grę na postoju taksówek.
accusedSuspects = []  # Oskarżeni podejrzani nie będą dawać wskazówek.
liars = random.sample(SUSPECTS, random.randint(3, 4))
accusationsLeft = 3  # Możesz oskarżyć maksymalnie 3 osoby.
culprit = random.choice(SUSPECTS)

# Te same indeksy łączą podejrzanego, przedmiot i miejsce.
random.shuffle(SUSPECTS)
random.shuffle(ITEMS)
random.shuffle(PLACES)

# Utwórz strukturę danych dla wskazówek o przedmiocie i podejrzanym,
# podanych przez osoby prawdomówne.
# Słownik ze wskazówkami (clues), gdzie klucze to podejrzani proszeni o wskazówkę, a wartościami słownik z daną wskazówką.
clues = {}
for i, interviewee in enumerate(SUSPECTS):
    if interviewee in liars:
        continue  # Na tym etapie pomiń kłamców.

    # Kluczami słownika wskazówek są przedmioty i podejrzani,
    # a wartością jest podana wskazówka.
    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = False  # Przydatne podczas rozwiązywania problemów.
    for item in ITEMS:  # Wybierz wskazówkę o każdym przedmiocie.
        if random.randint(0, 1) == 0:  # Powiedz, gdzie jest dany przedmiot:
            clues[interviewee][item] = PLACES[ITEMS.index(item)]
        else:  # Powiedz, kto ma dany przedmiot:
            clues[interviewee][item] = SUSPECTS[ITEMS.index(item)]
    for suspect in SUSPECTS:  # Wybierz wskazówkę o każdym podejrzanym.
        if random.randint(0, 1) == 0:  # Powiedz, gdzie jest podejrzany:
            clues[interviewee][suspect] = PLACES[SUSPECTS.index(suspect)]
        else:  # Powiedz, jaki przedmiot ma dany podejrzany:
            clues[interviewee][suspect] = ITEMS[SUSPECTS.index(suspect)]

# Utwórz strukturę danych dla wskazówek podanych przez kłamców
# na temat każdego przedmiotu i podejrzanego:
for i, interviewee in enumerate(SUSPECTS):
    if interviewee not in liars:
        continue  # Już mamy obsługę osób prawdomównych.

    # Kluczami słownika wskazówek są przedmioty i podejrzani,
    # a wartością jest podana wskazówka.
    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = True  # Przydatne podczas rozwiązywania problemów.

    # Ten podejrzany jest kłamcą i podaje błędne wskazówki:
    for item in ITEMS:
        if random.randint(0, 1) == 0:
            while True:  # Wybierz losowe (błędne) miejsce związane ze wskazówką.
                # Kłamie na temat miejsca przedmiotu.
                clues[interviewee][item] = random.choice(PLACES)
                if clues[interviewee][item] != PLACES[ITEMS.index(item)]:
                    # Wyjdź z pętli po wybraniu błędnej wskazówki.
                    break
        else:
            while True:  # Wybierz losowego (błędnego) podejrzanego związanego ze wskazówką.
                clues[interviewee][item] = random.choice(SUSPECTS)
                if clues[interviewee][item] != SUSPECTS[ITEMS.index(item)]:
                    # Wyjdź z pętli po wybraniu błędnej wskazówki.
                    break
    for suspect in SUSPECTS:
        if random.randint(0, 1) == 0:
            while True:  # Wybierz losowe (błędne) miejsce związane ze wskazówką.
                clues[interviewee][suspect] = random.choice(PLACES)
                if clues[interviewee][suspect] != PLACES[ITEMS.index(item)]:
                    # Wyjdź z pętli po wybraniu błędnej wskazówki.
                    break
        else:
            while True:  # Wybierz losowy (błędny) przedmiot związany ze wskazówką.
                clues[interviewee][suspect] = random.choice(ITEMS)
                if clues[interviewee][suspect] != ITEMS[SUSPECTS.index(suspect)]:
                    # Wyjdź z pętli po wybraniu błędnej wskazówki.
                    break

# Utwórz strukturę danych dla wskazówek otrzymanych po zapytaniu o kota Zophie:
zophieClues = {}
for interviewee in random.sample(SUSPECTS, random.randint(3, 4)):
    kindOfClue = random.randint(1, 3)
    if kindOfClue == 1:
        if interviewee not in liars:
            # Oni Ci powiedzą, gdzie jest Zophie.
            zophieClues[interviewee] = culprit
        elif interviewee in liars:
            while True:
                # Wybierz błędną wskazówkę podejrzanego.
                zophieClues[interviewee] = random.choice(SUSPECTS)
                if zophieClues[interviewee] != culprit:
                    # Wyjdź z pętli po wybraniu błędnej wskazówki.
                    break

    elif kindOfClue == 2:
        if interviewee not in liars:
            # Oni Ci powiedzą, gdzie jest Zophie.
            zophieClues[interviewee] = PLACES[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                # Wybierz błędną wskazówkę na temat miejsca.
                zophieClues[interviewee] = random.choice(PLACES)
                if zophieClues[interviewee] != PLACES[SUSPECTS.index(culprit)]:
                    # Wyjdź z pętli po wybraniu błędnej wskazówki.
                    break
    elif kindOfClue == 3:
        if interviewee not in liars:
            # Oni Ci powiedzą, jaki przedmiot znajduje się blisko Zophie.
            zophieClues[interviewee] = ITEMS[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                # Wybierz błędną wskazówkę na temat przedmiotu.
                zophieClues[interviewee] = random.choice(ITEMS)
                if zophieClues[interviewee] != ITEMS[SUSPECTS.index(culprit)]:
                    # Wyjdź z pętli, gdy zostanie wybrana błędna wskazówka.
                    break

# EKSPERYMENT: Usuń znaczniki komentarz z przed tego bloku kodu, by zobaczyć strukturę danych dla wskazówek:
#import pprint
#pprint.pprint(clues)
#pprint.pprint(zophieClues)
#print('culprit =', culprit)

# POCZĄTEK GRY
print("""OSKARŻAM! (gra detektywistyczna)")
Autor: Al Sweigarta, al@inventwithpython.com
Program zainspirowany grą Where's the EGG?)

Jesteś światowej sławy detektywem, Matyldą Camus. 
Zaginął kot Zophie, a Ty musisz dokładnie zbadać wszystkie wskazówki. P
Podejrzani albo zawsze kłamią, albo zawsze mówią prawdę. Zadawaj im pytania
o innych ludzi, miejsca i przedmiotyach, by określić, czy szczegóły
przez niche podawane są wartegodne zaufania i zgodne z Twoimi obserwacjami.
Dzięki temu będziesz wiedzieć, czy ich wskazówka o kocie Zophie jest prawdziwa, czy nie. Czy znajdziesz kota Zophie
na czas i oskarżysz winnego?
""")
input('Naciśnij Enter, aby rozpocząć...')


startTime = time.time()
endTime = startTime + TIME_TO_SOLVE

while True:  # Główna pętla gry.
    if time.time() > endTime or accusationsLeft == 0:
        # Obsługa warunku końca gry:
        if time.time() > endTime:
            print('Skończył Ci się czas!')
        elif accusationsLeft == 0:
            print('Oskarżyłeś zbyt wielu niewinnych ludzi!')
        culpritIndex = SUSPECTS.index(culprit)
        print('Kota porwał {} w miejscu: {} z: {}!'.format(culprit, PLACES[culpritIndex], ITEMS[culpritIndex]))
        print('Może następnym razem będziesz miał więcej szczęścia, Detektywie.')
        sys.exit()

    print()
    minutesLeft = int(endTime - time.time()) // 60
    secondsLeft = int(endTime - time.time()) % 60
    print('Pozostało: {} min, {} sek.'.format(minutesLeft, secondsLeft))

    if currentLocation == 'TAXI':
        print('  Jesteś w swojej TAXI. Dokąd chcesz jechać?')
        for place in sorted(PLACES):
            placeInfo = ''
            if place in visitedPlaces:
                placeInfo = visitedPlaces[place]
            nameLabel = '(' + place[0] + ')' + place[1:]
            spacing = " " * (LONGEST_PLACE_NAME_LENGTH - len(place))
            print('{} {}{}'.format(nameLabel, spacing, placeInfo))
        print('(K)ONIEC GRY')
        while True:  # Pytaj, dopóki nie zostanie podana odpowiednia odpowiedź.
            response = input('> ').upper()
            if response == '':
                continue  # Zapytaj ponownie.
            if response == 'K':
                print('Dziękujemy za grę!')
                sys.exit()
            if response in PLACE_FIRST_LETTERS.keys():
                break
        currentLocation = PLACE_FIRST_LETTERS[response]
        continue  # Wróć do początku głównej pętli gry.

    # Będąc na miejscu, gracz może pytać o wskazówki.
    print('  Jesteś w miejscu: {}.'.format(currentLocation))
    currentLocationIndex = PLACES.index(currentLocation)
    thePersonHere = SUSPECTS[currentLocationIndex]
    theItemHere = ITEMS[currentLocationIndex]
    print('  Jest tutaj {} z: {}.'.format(thePersonHere, theItemHere))

    # Dodaj podejrzanego i przedmiot znajdujących się w tym miejscu do naszej listy
    # znanych nam już podejrzanych i przedmiotów:
    if thePersonHere not in knownSuspectsAndItems:
        knownSuspectsAndItems.append(thePersonHere)
    if ITEMS[currentLocationIndex] not in knownSuspectsAndItems:
        knownSuspectsAndItems.append(ITEMS[currentLocationIndex])
    if currentLocation not in visitedPlaces.keys():
        visitedPlaces[currentLocation] = '({}, {})'.format(thePersonHere.lower(), theItemHere.lower())

    # Jeśli gracz wcześniej niesłusznie oskarżył tę osobę,
    # to nie otrzyma od niej wskazówki:
    if thePersonHere in accusedSuspects:
        print('Są obrażeni, że ich oskarżyłeś,')
        print('dlatego nie pomogą Ci w Twoim śledztwie.')
        print('Wracasz do swojej TAXI.')
        print()
        input('Naciśnij Enter, aby kontynuować...')
        currentLocation = 'TAXI'
        continue  # Wróć do początku głównej pętli gry.

    # Wyświetl menu z podejrzanymi i przedmiotami, o które gracz może spytać:
    print()
    print('(O) "OSKARŻAM!" (Pozostało {} oskarżeń)'.format(accusationsLeft))
    print('(Z) Spytaj, czy wiedzą, gdzie jest kot Zophie.')
    print('(T) Wróć do TAXI.')
    for i, suspectOrItem in enumerate(knownSuspectsAndItems):
        print('({}) Zapytaj o: {}'.format(i + 1, suspectOrItem))

    while True:  # Pytaj, dopóki nie zostanie podana odpowiednia odpowiedź.
        response = input('> ').upper()
        if response in 'OZT' or (response.isdecimal() and 0 < int(response) <= len(knownSuspectsAndItems)):
            break

    if response == 'O':  # Gracz oskarża tego podejrzanego.
        accusationsLeft -= 1  # Zużył jedno oskarżenie.
        if thePersonHere == culprit:
            # Gracz słusznie oskarżył podejrzanego.
            print('Rozwiązałeś sprawę, Detektywie!')
            print('Kota Zophie porwał(a) {}.'.format(culprit))
            minutesTaken = int(time.time() - startTime) // 60
            secondsTaken = int(time.time() - startTime) % 60
            print('Dobra robota! Rozwiązałeś sprawę w {} min, {} sek.'.format(minutesTaken, secondsTaken))
            sys.exit()
        else:
            # Gracz niesłusznie oskarżył daną osobę.
            accusedSuspects.append(thePersonHere)
            print('Oskarżyłeś niewinną osobę, Detektywie!')
            print('Nie otrzymasz od niej już żadnych wskazówek.')
            print('Wracasz do swojej TAXI.')
            currentLocation = 'TAXI'

    elif response == 'Z':  # Gracz pyta o Zophie.
        if thePersonHere not in zophieClues:
            print('"Nic nie wiem o kocie Zophie."')
        elif thePersonHere in zophieClues:
            print('  Podejrzany daje Ci taką wskazówkę: "{}"'.format(zophieClues[thePersonHere]))
            # Dodaj wskazówkę niezwiązaną z miejscem do listy znanych rzeczy:
            if zophieClues[thePersonHere] not in knownSuspectsAndItems and zophieClues[thePersonHere] not in PLACES:
                knownSuspectsAndItems.append(zophieClues[thePersonHere])

    elif response == 'T':  # Gracz wraca do taksówki.
        currentLocation = 'TAXI'
        continue  # Wróć do początku głównej pętli gry.

    else:  # Gracz pyta o podejrzanego lub przedmiot.
        thingBeingAskedAbout = knownSuspectsAndItems[int(response) - 1]
        if thingBeingAskedAbout in (thePersonHere, theItemHere):
            print('  Otrzymujesz następującą wskazówkę: "Brak komentarza."')
        else:
            print('  Otrzymujesz następującą wskazówkę: "{}"'.format(clues[thePersonHere][thingBeingAskedAbout]))
            # Dodaj wskazówkę niezwiązaną z miejscem do listy znanych rzeczy:
            if clues[thePersonHere][thingBeingAskedAbout] not in knownSuspectsAndItems and clues[thePersonHere][thingBeingAskedAbout] not in PLACES:
                knownSuspectsAndItems.append(clues[thePersonHere][thingBeingAskedAbout])

    input('Naciśnij Enter, by kontynuować...')
