# # Der User wird nach einer Zahl gefragt und es soll ausgegeben werden ob die Zahl = < oder > 10

# # Der User wird nach einer Zahl gefragt. Es soll geprüft werden ob es eine gerade oder ungerade Zahl ist

# Schreibe ein Programm, das den Benutzer nach einem Passwort fragt und prüft, ob es mindestens 8 Zeichen lang ist.

# Der User wird nach einer Zahl zwischen 1-7 gefragt
# 1 Montag 2 Dienstag 3 Mittwoch 4 Donnerstag 5 Freitag 6 Samstag 7 Sonntag
# Bei anderen eingaben "keine gültige Eingabe"

# Der User wird nach seiner Punktzahl gefragt
# sehr gut 100 - 92
# gut       91 - 81
# befriedigend 80 - 67
# ausreichend 66 - 50
# mangelhaft 49 - 30
# ungenügend 29 - 0
# Bei anderen eingaben "keine gültige Eingabe"

#AUFGABE 1

zahl = 10

if(zahl < 10):
    print("kleiner als 10")
elif(zahl == 10):
    print("gleich 10")
elif(zahl > 10):
    print("größer als 10")


#AUFGABE 2
zahl = input(f"Bitte geben Sie eine Zahl ein")
zahl = int(zahl)
if (zahl % 2 == 0):
    print("gerade")
else:
    print("ungerade")

#AUFGABE 3

passwort = input(f"Guten Tag, bitte geben Sie Ihr Passwort ein:")
if len(passwort) < 8:
        print ("Das Passwort ist zu kurz, mindestens 8 Zeichen!")
else:
        print("OK")

#Aufgabe 4
zahl = input(f"Bitte geben Sie eine Zahl von 1-7 ein")
zahl = int(zahl)
if(zahl == 1):
    print("Montag")
elif(zahl == 2):
    print("Dienstag")
elif(zahl == 3):
    print("Mittwoch")
elif(zahl == 4):
    print("Donnerstag")
elif(zahl == 5):
    print("Freitag")
elif(zahl == 6):
    print("Samstag")
elif(zahl == 7):
    print("Sonntag")
else:
    print("keine gültige Angabe!")

#Aufgabe 5
punktzahl = int(input("Bitte geben Sie Ihre Punktzahl an:"))

if punktzahl <= 100 and punktzahl > 91:
    print("sehr gut")
elif punktzahl <= 91 and punktzahl > 80:
    print("gut")
elif punktzahl <= 80 and punktzahl > 66:
    print("befriedigend")
elif punktzahl <= 66 and punktzahl > 49:
    print("ausreichend")
elif punktzahl <= 49 and punktzahl > 29:
    print("mangelhaft")
elif punktzahl <= 29 and punktzahl > 0:
    print("ungenügend")
elif punktzahl > 100 or punktzahl < 0:
    print("ERROR")