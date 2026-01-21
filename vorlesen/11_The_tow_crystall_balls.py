# Das ProblemDu stehst vor einem Hochhaus mit 100 Stockwerken. Du hast zwei identische Kristallkugeln. Du sollst
# herausfinden, ab welchem Stockwerk (dem "kritischen Stockwerk") die Kugeln zerbrechen, wenn man sie aus dem Fenster
# wirft.
# Wenn eine Kugel beim Wurf nicht zerbricht, kannst du sie wiederverwenden.
# Wenn sie zerbricht, ist sie weg.Du musst das kritische Stockwerk mit der minimalen Anzahl an Würfen finden.
import random
from itertools import count

kritisch = random.randint(0, 100)
haus = list(range(101))
kugel1 = haus[100]
kugel2 = haus[0]


while kugel2 <= kugel1:

    mitte = len(haus) // 2
    if kugel1 == kritisch:
        print(f'Deine erste Kugel wurde zerstört auf etage {kritisch}')
    elif kugel2 == kritisch:
        print(f'Deine zweite Kugel wurde zerstört auf etage {kritisch}')

    if haus[mitte] == kritisch:
        break
    elif haus[mitte] < kritisch:
        kugel2 = mitte + 1
    elif haus[mitte] > kritisch:
        kugel1 = mitte - 1

else:
    print(f'Der Kritische Stockwerk {kritisch} wurde zwischen {kugel2} und {kugel1} entdeckt.')
