#!/bin/env python3

# Erstelle eine Klasse Auto und definieren
class Auto:
    def __init__(self, ps, ccm, l_per_100km, modell):
        self.ps = ps
        self.ccm = ccm
        self.l_per_100km = l_per_100km
        self.modell = modell

# Erstelle ein Dictionary mit 3 Automarken, die jeweils 3 Modelle der Klasse Auto enthalten
# Ähnlich wie json aufgebaut
autos = {
    "Ford": [
        Auto(130, 1900, 8.5, "Focus"),
        Auto(300, 3500, 11.0, "Mustang"),
        Auto(98, 1300, 5.0, "Fiesta")
    ],
    "BMW": [
        Auto(250, 3000, 9.0, "X5"),
        Auto(300, 4000, 11.0, "M8"),
        Auto(400, 4500, 13.0, "Z4")
    ],
    "Audi": [
        Auto(170, 2000, 7.0, "A3"),
        Auto(245, 3000, 9.0, "Q6"),
        Auto(340, 3500, 11.0, "R8")
    ]
}

# Überprüfe, ob das Dictionary die Marke "Ford" enthält und gib sie aus
if "Ford" in autos:
    for auto in autos["Ford"]:
        print(f"Ford: {auto.modell}, PS: {auto.ps}, Hubraum: {auto.ccm} ccm, Verbrauch: {auto.l_per_100km} l/100km")