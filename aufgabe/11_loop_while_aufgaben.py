# Zahlen addieren:
# Schreibe eine While-Schleife,
# die die Summe von Zahlen von 1 bis zu einer vom Benutzer
# eingegebener Zahl berechnet.
zahl = 0
usereingabe = int(input(f'Bis zu welcher Zahl soll addiert werden? :'))

while usereingabe != 0:
    zahl += usereingabe
    usereingabe -= 1
print(zahl)


# Passwort überprüfen:
# Erstelle eine Schleife,
# die den Benutzer nach einem Passwort fragt,
# bis das korrekte Passwort eingegeben wird.
# password = 'G3h31m'
# frage = ''
# while frage != password:
#     frage = input('Bitte geben Sie das Passwort ein: ')
#     if frage == password:
#         print('come in')
#     else:
#         print('Falsche Eingabe')


# Ein Spieler soll eine (zufällig gewählte) Zahl zwischen 1 und 100 erraten.
# Das Programm soll jeweils die Meldungen „Die Zahl ist zu groß“,
# „Die Zahl ist zu klein“ bzw.
# „Treffer“ ausgeben.
# Wenn die Zahl zu Gross oder zu klein ist soll die Frage erneut gestellt werden

import random

zufall_zahl = random.randint(1, 100)
eingabe = ''
print(zufall_zahl)
while eingabe != zufall_zahl:
    eingabe = int(input('Errate die Zahl: '))
    if eingabe < zufall_zahl:
        print('Die Zahl ist zu klein')
    elif eingabe > zufall_zahl:
        print('Die Zahl ist zu gross')
    else:
        print('Treffer')
