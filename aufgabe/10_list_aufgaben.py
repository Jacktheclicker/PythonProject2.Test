# Erstellen Sie eine Liste von 5 Städten, die Sie besuchen möchten.
stadt_liste = ["thessaloniki", "beirut", "karthum", "caracas", "gaza"]
# Fügen Sie dann eine weitere Stadt hinzu und entfernen Sie die dritte Stadt aus der Liste.
stadt_liste.append("kabul")
stadt_liste.pop(2)
# Schließlich geben Sie die Liste der verbleibenden Städte aus.
print(stadt_liste)

# Erstelle eine Liste super_liste mit folgenden Items: 20, 50.5, 'Hallo', True, 'Löschen', 'auf Wiedersehen'
liste = [20, 50.5, "Hallo", True, "löschen", "auf Wiedersehen"]
# Ändere den Wert des ersten Elementes zu 95
liste[0] = 95
# Kopiere den Wert des 4 Items auf den 2 index
liste[2] = liste[3]
# Ändere das 4 Element zu False
liste[3] = False
# Füge das Element "999" an der letzten Stelle der Liste an
liste.append("999")
# Füge das Element "Nummer 5" an der 5 Stelle ein
liste.insert(4, "Nummer 5")
# tauche das Element mit dem Index 0 und das Index 5
liste[0], liste[5] = liste[5], liste[0]
# Schreibe eine If anweisung die das Element 'bin da' löscht, wenn es vorhanden ist.
# Wenn das Element nicht vorhanden ist, soll es an letzter Stelle hinzugefügt werden
if "bin da" in liste:
    liste.remove("bin da")
else:
    liste.append("bin da")
# copy die liste in die Variable list_copy
list_copy = liste.copy()
# Leere die Originalliste
liste.clear()
# Füge die letzten 3 Elemente der list_copy an die super_liste an.
liste.extend(stadt_liste.copy[-3:])
print(liste)
