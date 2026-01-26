# Das ProblemDu stehst vor einem Hochhaus mit 100 Stockwerken. Du hast zwei identische Kristallkugeln. Du sollst
# herausfinden, ab welchem Stockwerk (dem "kritischen Stockwerk") die Kugeln zerbrechen, wenn man sie aus dem Fenster
# wirft.
# Wenn eine Kugel beim Wurf nicht zerbricht, kannst du sie wiederverwenden.
# Wenn sie zerbricht, ist sie weg.Du musst das kritische Stockwerk mit der minimalen Anzahl an Würfen finden.
import random
from itertools import count

kritisch = random.randint(0, 100)
haus = list(range(101))
ball_1 = True
ball_2 = True
wurf_aus = len(haus)//2
if wurf_aus >= kritisch:
    ball_1 = False
    print('kugel kaputt')
kugel1 = len(haus) -1
kugel2 = 0
count = 0
print(haus)
while kugel2 <= kugel1:
    count +=1
    mitte = (kugel1 + kugel2) // 2

    if haus[mitte] == kritisch:
        print(f'Das kritische Stockwerk ist {kritisch}. gefunden bei runde {count}')
        break
    elif haus[mitte] < kritisch:
        kugel2 = haus[mitte + 1]
    else:
        kugel1 = haus[mitte - 1]

else:
    print(f'Der Kritische Stockwerk {kritisch} wurde zwischen {kugel2} und {kugel1} entdeckt.{count}')
