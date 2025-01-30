# einkaufsliste = []
# wahl = "y"

# while wahl == "y":
    # einkaufsliste.append(input("was möchtest du hinzufügen?"))
    # wahl = input("Möchtest du weitere Artikel hinzufügen? (y / n) ")

    # print (einkaufsliste)

# KOMPLEXERE VARIANTE:
# Artikel hinzufügen
# Aktion -> hinzufügen, entfernen, anzeigen, beenden

einkaufsliste = []

while True:
    aktion = input('Möchtest du einen Artikel hinzufügen, entfernen oder die Liste anzeigen? ("hinzufügen / entfernen / anzeigen / beenden")')
    
    # hinzufügen
    if aktion == "hinzufügen":
        artikel = input("welchen Artikel möchtest du hinzufügen? ")
        einkaufsliste.append(artikel)
        print("Artikel wurde hinzugefügt")

    # entfernen
    elif aktion == "entfernen":
        artikel = input("welchen Artikel möchtest du entfernen? ")
        if artikel in einkaufsliste:
            einkaufsliste.remove(artikel)
            print("Artikel wurde gelöscht")
        else:
            print("Artikel konnte nicht gefunden werden")

    # anzeigen
    elif aktion == "anzeigen":
        print("Übersicht deiner Einkaufsliste:")
        print(einkaufsliste)

    # beenden
    elif aktion == "beenden":
        print("Vorgang wurde beendet")
        break # mit break wird die Schleife untebrochen

    else: # falls man vertippt hat
        print("fehlerhafte Eingabe!")
