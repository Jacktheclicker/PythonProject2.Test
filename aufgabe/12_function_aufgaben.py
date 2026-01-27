import math


# Schreibe eine Funktion zur Berechnung der Fläche eines Quadrates
def quadrat(a):
    quadrat = math.sqrt(a**2)
    return quadrat


# Schreibe eine Funktion zur Berechnung der Fläche eines Rechteckes
def rechteck(a , b):
    rechteck = math.sqrt(a*2 + b*2)
    return rechteck


# Schreibe eine Funktion zur Berechnung der Fläche eines Kreises
pi = float(3.14159)
r = float
def kreis(pi , r):
    kreis = math.sqrt(pi * r**2)
    return kreis


# Schreibe eine Funktion die 2 Zahlen als übergabe Parameter bekommt und die größere Zahl wieder gibt

def übergabe_groeßer(a , b):
    if a > b:
        return a
    else:
        return b

# Schreibe eine Funktion die überprüft, ob eine Zahl positiv negativ oder null ist.
def prüfer(a):
    a = int(a)
    if a < 0:
        return ('Negative')
    elif a > 0:
        return ('Positive')
    else:
        return ('Null')




