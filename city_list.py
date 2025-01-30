#!/bin/env python3

# Erstellt einen Liste mit städtenamen
cities = [
    "Prag", "Berlin", "Paris", "Brüssel", "Moskau", "Dubai", "Amsterdam", "Ankara", "Warschau", "Pekin", "Tokyo"
    ]

# Sortiert diese Liste
cities.sort()

# checkt mit contains ob 2 städte enthalten sind
city1 = "Moskau"
city2 = "Dubai"

# gebt diese städte ins terminal aus
if city1 in cities and city2 in cities:
    print(f"{city1} und {city2} sind in der Liste.")
else:
    print(f"{city1} und {city2} sind nicht in der Liste.")


# Macht ein tupel mit vornamen
vornamen = (
    "Arthur", "Muhammed", "Talha", "Emre", "Stephan"
    )

# macht ein tupel mit nachnamen
nachnamen = (
    "Deynes", "Bagci", "Uenlue", "Coskun", "Loecher"
    )

# verbidnet vor und nachname für die email mit einem punkt (join methode)
domain = "@skyered.de"

emails = [f"{vorname}.{nachname}{domain}" for vorname, nachname in zip(vornamen, nachnamen)]
# Die zip-Funktion nimmt den ersten Vornamen und den ersten Nachnamen und macht daraus ein Paar


# Ausgabe der E-Mail-Adressen
for email in emails:
    print(email)


