from Controller.Logic import suche_helme

def getInput():
    print("===== Motorradhelm-Suche =====")
    groesse = input("Wähle bitte eine Helmgröße (S, M, L, XL) oder leer lassen: ") or None
    max_preis = input("Maximaler Preis (€) oder leer lassen: ")
    max_preis = int(max_preis) if max_preis else None
    art = input("Helmart (Sport, Enduro, Cruiser, Jethelm, Klapphelm) oder leer lassen: ") or None
    verschluss = input("Verschlussart (Ratsche, Doppel-D) oder leer lassen: ") or None
    material = input("Material (Fiberglas, Carbon, Polycarbonat) oder leer lassen: ") or None

    ergebnisse = suche_helme(groesse, max_preis, art, verschluss, material)

    print("\n===== Gefundene Helme =====")
    for helm in ergebnisse:
        print(helm)

if __name__ == "__main__":
    getInput()
