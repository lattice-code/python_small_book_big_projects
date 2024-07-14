"""Symulacja paska postępu, autor: Al Sweigart, al@inventwithpython.com
Przykładowa animacja paska postępu, która może być użyta w innych programach.
Kod pobrany ze strony https://ftp.helion.pl/przyklady/wiksma.zip.
Etykiety: króciutki, moduł"""

import random, time

BAR = chr(9608) # Znak 9608 to '█'.

def main():
    # Symulacja pobierania pliku:
    print('Symulacja paska postępu, autor: Al Sweigart')
    bytesDownloaded = 0
    downloadSize = 4096
    while bytesDownloaded < downloadSize:
        # "Pobierz" losową liczbę "bajtów":
        bytesDownloaded += random.randint(0, 100)

        # Ustaw pasek postępu w formie łańcucha znaków dla bieżącego etapu:
        barStr = getProgressBar(bytesDownloaded, downloadSize)

        # Nie wyświetlaj znaku nowej linii na końcu i natychmiast usuń
        # z ekranu wyświetlony łańcuch znaków:
        print(barStr, end='', flush=True)

        time.sleep(0.2)  # Zatrzymaj się na chwilę.

        # Za pomocą znaków backspace przesuń kursor na początek linii:
        print('\b' * len(barStr), end='', flush=True)


def getProgressBar(progress, total, barWidth=40):
    """Zwraca łańcuch znaków przedstawiający pasek o szerokości równej wartości zapisanej w zmiennej barWidth
    i zapełniony w stopniu odzwierciedlającym postęp wykonania zadania."""

    progressBar = ''  # Pasek postępu będzie łańcuchem znaków.
    progressBar += '['  # Utwórz lewą część paska postępu.

    # Upewnij się, że postęp jest równy liczbie z zakresu od 0 do wartości zapisanej w zmiennej total:
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    # Oblicz liczbę elementów paska do wyświetlenia:
    numberOfBars = int((progress / total) * barWidth)

    progressBar += BAR * numberOfBars  # Dodaj pasek postępu.
    progressBar += ' ' * (barWidth - numberOfBars)  # Dodaj spacje.
    progressBar += ']'  # Dodaj prawy koniec paska postępu.

    # Oblicz procent postępu:
    percentComplete = round(progress / total * 100, 1)
    progressBar += ' ' + str(percentComplete) + '%'  # Dodaj procent.

    # Dodaj liczby:
    progressBar += ' ' + str(progress) + '/' + str(total)

    return progressBar  # Zwróć pasek postępu w postaci łańcucha znaków.


# Jeśli program został uruchomiony (a nie zaimportowany), rozpocznij grę:
if __name__ == '__main__':
    main()
