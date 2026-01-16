
# Erstelle eine list tic
tic = []
# Füge tic eine Liste mit den werten 'l','l','l' hinzu
tic = ['l', 'l', 'l'] , ['k', 'k', 'k'] , ['b', 'b', 'b']

# Füge tic eine 2. liste mir den werten 'k','k','k' hinzu
# Füge tic eine 3. liste mir den werten 'b','b','b' hinzu

# Printe jede unterliste in einer Zeile aus
# ['l', 'l', 'l']
# ['k', 'k', 'k']
# ['b', 'b', 'b']

# ändere die liste wie folgt ab
# ['x', 'l', 'l']
# ['k', 'x', 'k']
# ['b', 'b', 'x']
tic[0][0] = "x"
tic[1][1] = "x"
tic[2][2] = "x"

# ändere die liste wie folgt ab
# ['x', 'o', 'o']
# ['x', 'x', 'o']
# ['o', 'x', 'o']
tic[0][1] = "o"
tic[0][2] = "o"
tic[1][0] = "x"
tic[1][1] = "x"
tic[1][2] = "o"
tic[2][0] = "o"
tic[2][1] = "x"
tic[2][2] = "o"

# ändere die liste wie folgt ab
# ['o', 'o', 'o']
# ['x', 'x', 'o']
# ['o', 'x', 'o']
tic[0][0] = "o"
# schriebe ein Programm das 2 Zahlen zwischen 1 und 3 und einem Buchstaben vom user fordert
# zahl1 = int(input("Geben Sie bitte die erste Zahl zwischen 1 und 3 ein:  "))
# zahl2 = int(input("Geben Sie bitte die zweite Zahl zwischen 1 und 3 ein:  "))
# buchstabe = input("Bitte geben Sie einen Buchstaben ein:  ")
# Anschliessend soll der Wert mit der Pos der zwei Zahlen mit den Buchstaben überschrieben werden
# und die Liste wie in der vorherigen Aufgabe ausgegeben werden
# 1['o', 'o', 'o']
# 2['x', 'x', 'o']
# 3['o', 'x', 	'o']
# #    a    b    c
x_wert = int(input("x_wert von 1-3: \n")) -1
y_wert = int(input("y_wert von 1-3: \n")) -1
zeichen = input("zeichen x oder o: \n").lower()
# Beispiel Zahl1 = 3 Zahl2 = 2 Buchstabe = p
# 1['o', 'o', 'o']
# 2['x', 'x', 'p']
# 3['o', 'x', 'o']
# if y_wert == 1:
#     y_wert = 2
# elif    y_wert == 2:
#         y_wert = 1
# elif    y_wert == 3:
#         y_wert = 0

tic[y_wert][x_wert] = zeichen

# Zähle alle "o" in der mittleren Liste index 1
x = 0
if tic[1][0] == "o":
    x += 1
if tic[1][1] == "o":
    x += 1
if tic[1][2] == "o":
    x += 1

print(x)

#Schreib eine If anweisung die 'Sieg' ausgibt wenn das Zeiche auf pos 1.1 das selbe ist wie auf pos 2.2 und 3.3
if tic[0][0] ==  tic[1][1] ==  tic[2][2] == "o":
    print("Sieger!")
else:
    print("Looser!")


print(*tic, sep="\n")