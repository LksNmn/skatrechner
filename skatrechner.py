spielerAnzahl = 0
punkte = []
differenzen = []
i = 1
punktwert = 0.0

while spielerAnzahl <= 2:
    try:
        spielerAnzahl = int(input('Anzahl der Spieler: '))
    except ValueError:
            print("Nur positive ganze Zahlen eingeben")

while punktwert <= 0.0:
    try:
        punktwert = float(input('Punktwert: '))
    except ValueError:
        print("Nur positive Zahlen eingeben")

while len(punkte) < spielerAnzahl:
    try:
        punkte.append(int(input('Punktzahl von Spieler ' + str(i) + ': ')))
        i += 1
    except ValueError:
        print("Bitte nur ganze Zahlen eingeben")

for i in range(spielerAnzahl):
    gewinn, verlust, bilanz = 0,0,0
    copy = list(punkte)
    del copy[i]
    differenzen = ([punkte[i] - j for j in copy])
    for differenz in differenzen:
        if differenz <= 0:
            verlust += differenz
        else:
            gewinn += differenz
        bilanz += differenz
    #print("Spieler " + str(i + 1) + " gewinnt " + str(gewinn) + " und zahlt " + str(-verlust))
    print("Spieler " + str(i + 1) + (" gewinnt " if bilanz >= 0 else " zahlt ") + str(abs(bilanz * punktwert)))
