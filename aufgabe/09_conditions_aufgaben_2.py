# Der Benutzer soll zwei Zahlen in das Programm eingeben, danach soll er entscheiden, ob die Zahlen addiert,
# subtrahiert, multipliziert oder dividiert werden, diese Entscheidung soll über die Eingabe der folgenden
# Symbole getätigt werden + - * /:
# Bei der Division durch 0 soll die Ausgabe "Das kann nur Chuck Norris" erfolgen
# Nach der Auswahl soll das Ergebnis der Rechnung ausgegeben werden,
# bzw. eine Fehlermeldung, falls eine
# falsche Auswahl getroffen wurde.
#from multiprocessing.connection import arbitrary_address

# zahl1 = int(input("  "))
# operation = input("   ")
# zahl2 = int(input("  "))



# if operation == "+":
#     result = (float(zahl1)) + (float(zahl2))
#     print(f"{zahl1} {operation} {zahl2} = {result}")
# elif operation == "-":
#     result = (float(zahl1)) - (float(zahl2))
#     print(f"{zahl1} - {zahl2} = {result}")
# elif operation == "*":
#     result = (float(zahl1)) * (float(zahl2))
#     print(f"{zahl1} * {zahl2} = {result}")
# elif operation == "/" and float(zahl2) != 0:
#     result = (float(zahl1)) / (float(zahl2))
#     print(f"{zahl1} {operation} {zahl2} = {result}")
# elif operation == "/" and float(zahl2) == 0:
#     print(f"Das kann nur Space Jesus!")
#
# else:
#     print("geh nach hause jung")

# Nach dem Ohmschen Gesetz berechnet sich der Widerstand eines ohmschen Widerstandes mit:
# U = R * I
# R = U/I
# I = U/R
# Schreiben Sie ein Programm, in das der Benutzer zunächst über die Eingabe der Buchstaben R, U oder I
# auswählen kann, welche Größe berechnet werden soll. Gibt er einen falschen Buchstaben ein, soll eine Meldung
# über die Fehleingabe erfolgen.
# Anschließend soll er die Werte der fehlenden Größen eingeben. Am Ende gibt das Programm den Wert der
# gesuchten Größe mit der richtigen Einheit aus

# formelberechnung = input("Was möchten Sie berechnen? (Eingabe in Großbuchstaben) \nU = Spannung \nR = Widerstand \nI = Stromstärke \n" " ")
#
# if formelberechnung == "R":
#     U = float(input("Bitte geben Sie den Wert von U ein"))
#     I = float(input("Bitte geben Sie den Wert von I ein"))
#     R = U / I
#     print(f"Der Wert von R beträgt {R}.")
#
# elif formelberechnung == "U":
#     R = float(input("Bitte geben Sie den Wert von R ein"))
#     I = float(input("Bitte geben Sie den Wert von I ein"))
#     U = R * I
#     print(f"Der Wert von U beträgt {U}")
#
# elif formelberechnung == "I":
#     U = float(input("Bitte geben Sie den Wert von U ein"))
#     R = float(input("Bitte geben Sie den Wert von R ein"))
#     I = U / R
#     print(f"Der Wert von I beträgt {I}")
#
# else:
#     print("gehört nicht zur Berechnung")

# Ein Hardware-Großhändler führt ein Rabattsystem für Stammkunden ein: Liegt der Bestellwert zwischen 0 und
# 100 €, erhält der Kunde einen Rabatt von 10 %. Liegt der Bestellwert höher, aber insgesamt nicht über 500 €,
# beträgt der Rabatt 15 %, in allen anderen Fällen beträgt der Rabatt 20 %. Nach Eingabe des Bestellwertes soll
# der ermäßigte Bestellwert berechnet und ausgegeben werden.

# bestellwert = float(input("Bitte geben Sie Ihren Bestellwert an:"))
# if  bestellwert < 0:
#     print("Falsche Eingabe")
#
# elif bestellwert <= 100:
#     rabatt = 0.10
#     print(bestellwert - (bestellwert * rabatt))
#
# elif bestellwert <= 500:
#     rabatt = 0.15
#     print(bestellwert - (bestellwert * rabatt))
#
# elif bestellwert >= 501:
#     rabatt = 0.20
#     print(bestellwert - (bestellwert * rabatt))
#
# else:
#     print("Falsche Eingabe")

# Der BMI berechnet sich aus dem Körpergewicht [kg] dividiert durch das Quadrat der Körpergröße [m2
# Die Formel lautet: BMI = (Körpergewicht in kg): (Körpergröße in m)**2
# Der BMI einer Person wird nach den
# folgenden Regeln klassifiziert (nach DGE, Ernährungsbericht 1992):
# Klassifikation m w
# Untergewicht < 20 < 19
# Normalgewicht 20-25 19-24
# Übergewicht 25-30 24-30
# Adipositas 30-40 30-40
# massive Adipositas > 40 > 40
# Das Programm soll vom Benutzer das Gewicht [in kg] die Größe [in cm] und das Geschlecht [m/w] abfragen. Am
# Ende des Programms soll die BMI-Klassifikation der Person ausgegeben werden.
#
try:
    klassifikation = input("geben Sie bitte Ihr Geschlecht in M oder W an").upper()

    if klassifikation != "W" and klassifikation != "M":
        raise ValueError ("Ungültige Eingabe")


    körpergewicht = float(input("Bitte geben Sie Ihr Körpergewicht in Kg an: "))
    körpergröße = float(input("Bitte geben Sie Ihre Körpergröße in Meter an: "))
    bmi = körpergewicht / (körpergröße **2)


    if (klassifikation == "M" and bmi < 20) or (klassifikation == "W" and bmi < 19):
        print(f"Untergewicht {bmi}")
    elif (klassifikation == "M" and 20<= bmi <=25) or (klassifikation == "W" and 19<= bmi <=24):
        print(f"Normalgewicht {bmi}")
    elif (klassifikation == "M" and 25<= bmi <=30) or (klassifikation == "W" and 24<= bmi <=30):
        print(f"Übergewicht {bmi}")
    elif (klassifikation == "M" and 30<= bmi <=40) or (klassifikation == "W" and 30<= bmi <=40):
        print(f"Adipositas {bmi}")
    elif (klassifikation == "M" and 40<= bmi) or (klassifikation == "W" and  40<= bmi):
        print(f"massive Adipositas {bmi}")

    else:
        print("Ungültige Eingabe")
except:
    print("Geschlecht Falsch")

# Schaltjahres-Berechnung
# Eingabe eines Jahres -> Ausgabe Schaltjahr, kein Schaltjahr
# Laut Kalender hat ein Jahr 365 Tage. Die Erde braucht aber 365 Tage, 5 Stunden, 48 Minuten und 45 Sekunden,
# um die Sonne zu umrunden.
# Der Schalttag gleicht diese Differenz aus – allerdings nicht ganz, dazu sind die Zahlen zu unrund.
# Denn die überzähligen Stunden, Minuten und Sekunden addieren sich nach vier Jahren zu etwa 23 Stunden und 11 Minuten
# – also keinem ganzen Tag.
# Im Jahr 1582 veranlasste Papst Gregor eine Kalenderreform.
# Seitdem gilt der Gregorianische Kalender mit den folgenden Regeln zur Schaltjahresberechnung:
#
#
# jahr = int(input("Bitte geben Sie das Jahr ein: "))
# if jahr % 400 == 0 or jahr % 4 == 0 and jahr % 100 != 0:
#     print(f"{jahr} ist ein Schaltjahr")
#
# else:
#     print(f"{jahr} ist kein Schaltjahr")
#
# Bedingung 1:
# Ist eine Jahreszahl ganzzahlig durch 4 teilbar, dann ist das Jahr ein Schaltjahr. Testwerte: 1720, 1972
# und 1980 waren Schaltjahre.
# Bedingung 2:
# Ausnahme zu den Jahreszahlen, die der Bedingung 1 genügen, sind alle Jahreszahlen, die nach Bedingung 1
# ein Schaltjahr sind, aber deren Jahreszahl ganzzahlig durch 100 teilbar ist.
# Testwerte: 1700, 1800 und 1900 oder ferner 2100 sind keine Schaltjahre.
# Bedingung 3:
# Ausnahme zu den Jahreszahlen, die der Bedingung 2 genügen, sind alle Jahreszahlen, die nach Bedingung 2
# kein Schaltjahr sind, aber deren Jahreszahl ganzzahlig durch 400 teilbar.
# Testwerte: 1600 und 2000 waren Schaltjahre.



# Aufgabe: Berechnung der Energieverbrauchskosten
# Erstelle ein Programm, das die monatlichen Energiekosten eines Haushalts basierend auf dem Energieverbrauch berechnet.
# Dabei werden unterschiedliche Preise für verschiedene Verbrauchsstufen und ein Bonus für energiesparende Haushalte berücksichtigt.
#
# Berechnung:
# Basispreis:
#
# Für die ersten 100 kWh: 0,30 Euro pro kWh
# Für die nächsten 200 kWh (zwischen 101 kWh und 300 kWh): 0,25 Euro pro kWh
# Für den Verbrauch über 300 kWh: 0,20 Euro pro kWh
# Bonus für energiesparende Haushalte:
#
# Wenn der gesamte Verbrauch unter 150 kWh liegt, erhält der Haushalt einen Bonus von 10 Euro, der von den Gesamtkosten
# abgezogen wird.
# Das Programm sollte den Benutzer nach dem monatlichen Energieverbrauch in kWh fragen und dann die Gesamtkosten
# unter Berücksichtigung der oben genannten Bedingungen berechnen.

# verbrauch = float(input("Bitte geben Sie ihren Verbrauch in kWh"))
#
# if verbrauch <= 100:
#     print(f"Ihre Energieverbrauchskosten betragen:{verbrauch * 0.3 - 10} €")
#
# elif verbrauch <= 150:
#     print(f"Ihre Energieverbrauchskosten betragen: {(verbrauch - 100) * 0.25 + 100 * 0.3 -10} €")
#
# elif verbrauch <= 300:
#     print(f"Ihre Energieverbrauchskosten betragen: {(verbrauch - 200) * 0.25 + 200 * 0.25} €")
#
# elif verbrauch > 300:
#     print(f"Ihre Energieverbrauchskosten betragen: {(verbrauch - 300) * 0.20 + 200 * 0.25 + 100 * 0.3} €")
#
# else:
#     print("Falsche Eingabe")