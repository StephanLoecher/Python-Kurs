class Auto:
    """ Das ist meine Auto Klasse, sodass ich nicht alles neu definieren muss """
    def __init__(self, marke, modell, jahr, tueren, ps):
        self.marke = marke
        self.modell = modell
        self.jahr = jahr
        self.raeder = 4  # Standardwert für Räder
        self.tueren = tueren
        self.ps = ps

    def begruessung(self):
        print("Gute Wahl mit " + self.marke)


class Sportwagen(Auto):
    def __init__(self, marke, modell, jahr, tueren, ps, folierung):
        super().__init__(marke, modell, jahr, tueren, ps)
        self.folierung = folierung
        self.auspuff = 2

    def turbo(self):
        print("Turbo aktiviert!")


# Instanz eines Sportwagens erstellen
sw1 = Sportwagen(marke="Seat", modell="Ibiza", jahr=2020, tueren=2, ps=500, folierung="Rot")

# Teste Eigenschaften und Methoden
print(sw1.modell)           # Gibt "Ibiza" aus
sw1.turbo()                 # Gibt "Turbo aktiviert!" aus
sw1.begruessung()           # Gibt "Gute Wahl mit Seat" aus
