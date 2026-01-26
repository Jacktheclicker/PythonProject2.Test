# Berechne die Summe aller Zahlen von 1 - 500

print('Aufgabe 1')
# summe = 0
# for zahl in range(1,501):
#     summe += zahl
# print(summe)
print('#######################')

# Schreib eine Schleife die folgendes Muster ausgibt
# *
# **
# ***
# ****
# *****

print('Aufgabe 2')
# for schleife in range(1, 6):
#     print('*' * schleife)
print('#######################')


#
# # Schreib eine Schleife die folgendes Muster ausgibt
# # *****
# # ****
# # ***
# # **
# # *
print('Aufgabe 3')
# for schleife in range(5, 0, 1):
#     print('*' * schleife)
print('#######################')
#
# # Schreib eine Schleife, die folgendes Muster ausgibt
# # 1
# # 12
# # 123
# # 1234
# # 12345


print('Aufgabe 4')
# for zahl in range(1, 6):
#     for muster in range(1,zahl +1):
#         print(muster,end='')
#     print()


print('#######################')
#
# # Schreib eine Schleife, die folgendes Muster ausgibt
# # 5
# # 45
# # 345
# # 2345
# # 12345


print('Aufgabe 5')

# for zahl in range(5, 0, -1):
#     for muster in range(zahl, 6):
#         print(muster,end='')
#     print()
print('#######################')

# # Schreib eine Schleife, die folgendes Muster ausgibt
# # 12345
# # 1234
# # 123
# # 12
# # 1
print('Aufgabe 6')
# for zahl in range(5, 0, -1):
#     for m in range(1,zahl +1):
#         print(str(m) end='')
#     print()


print('#######################')
#
# # Der user soll zwei Zahlen angeben.
# # Bei der Eingabe von 6 und 2 soll folgendes Muster ausgegeben werden
# #
print('Aufgabe 7')
# zahl1 = int(input('bitte geben Sie die erste Zahl ein:  '))
# zahl2 = int(input('bitte geben Sie die zweite Zahl ein:  '))
#
# for zahl in range(zahl1):
#     print('*' * zahl2)
# for zahl in range(zahl2):
#     print('*' * zahl1)
# for zahl in range(1, zahl1, + 1):
#     print('*' * zahl)
# for zahl in range(zahl1, zahl1 - zahl2, -1):
#     print('*' * zahl)


# print(zahl)
print('#######################')
#
# #     **
# #     **
# #     **
# #     **
# #     **
# #     **
#
# #     ******
# #     ******
#
# #     *
# #     **
# #     ***
# #     ****
# #     *****
# #     ******
# #
#
#
# #     ******
# #     *****
# #
# # Bei
# # 7
# # und
# # 4
# #
# # ****
# # ****
# # ****
# # ****
# # ****
# # ****
# # ****
# #
# # *******
# # *******
# # *******
# # *******
# #
# # *
# # **
# # ***
# # ****
# # *****
# # ******
# # *******
# #
# # *******
# # ******
# # *****
# # ****
#
#
# # ### fizzbuzz
# # Schreiben Sie ein Programm, das die Zahlen von 1 bis 100 ausgibt.
# # Bei jeder Zahl, die durch 5 teilbar ist, soll "fizz" ausgegeben werden
# # und bei jeder Zahl, die durch 7 teilbar ist,
# # soll "buzz" ausgegeben werden.
# # Wenn die Zahl sowohl durch 7 als auch durch 5 teilbar ist,
# # soll "fizzbuzz" ausgegeben werden.
# # Der Modulo-Operator ermittelt den Rest bei Division.
# # Somit ist eine Teilbarkeit einfach dann erreicht,
# # wenn die Modulo-Operation (%, MOD) den Rest 0 liefert.
# print('Aufgabe 8')
for zahl in range(101):
        if zahl % 5 == 0 and zahl % 7 == 0:
            print('fizzbuzz')
        elif zahl % 5 == 0:
            print('fizz')
        elif zahl % 7 == 0:
            print('buzz')
        else:
            print(zahl)

print('#######################')
#
print('Aufgabe 9')
for zeile in range(8):
    for spalte in range(8):
        if (zeile + spalte) % 2 == 0:
            print('O', end='')
        else:
            print('X', end='')
    print()

print('#######################')
#
# # Schreib eine Schleife, die folgendes Muster ausgibt
# # OXOXOXOX
# # XOXOXOXO
# # OXOXOXOX
# # XOXOXOXO
# # OXOXOXOX
# # XOXOXOXO
# # OXOXOXOX
# # XOXOXOXO
