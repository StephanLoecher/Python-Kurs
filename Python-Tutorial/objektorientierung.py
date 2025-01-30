class Auto:
    """ Das ist meine Auto Klasse so dass ich nicht aufs neue definieren muss """
    def __init__(self, marke, modell, jahr, tueren, ps):
        self.marke = marke
        self.modell = modell
        self.jahr = jahr
        self.raeder = 4  # Standardwert für Räder
        self.tueren = tueren
        self.ps = ps

    def begruessung(self):
        print("Gute wahl mit "+ self.marke)


# Erstellen eines Auto-Objekts
auto1 = Auto(marke="Volkswagen", modell="Golf", jahr=2019, tueren=4, ps=100)
auto2 = Auto(marke="Volkswagen", modell="Toureg", jahr=2015, tueren=4, ps=200)
auto3 = Auto(marke="Porsche", modell="911", jahr=2014, tueren=4, ps=300)

print(auto1.marke)
print(auto2.marke)
print(auto3.marke)

auto1.begruessung()
auto2.begruessung()
auto3.begruessung()

