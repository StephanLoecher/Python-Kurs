class student:
    def __init__(self, name, age, interessen):
        self.name = name
        self.age = age
        self.interessen = interessen
        
Muhammed = student("Muhammed", 26, ["Kochen", "Fußball spielen"])
Arthur = student("Arthur", 24, ["Programmieren", "Computer zocken"]) 
Muhammed = student("Muhamme8d", 26, ["Kochen", "Fußball spielen"])



# Eingabe entgegennehmen
name = input("Gib euren Namen ein: ")

# Variable ausgeben
print("Dein Name lautet: ", name)


# Zwei Eingaben entgegennehmen
zahl1 = (input("Gib eine Zahl an: "))
zahl2 = (input("Gib eine Zahl an: "))

# Addition der Zwei Eingaben
ergebniss = int(zahl1) + int(zahl2)

# Variable ausgeben
print(f"Die {zahl1} wurden mit {zahl2} addiert das Ergebniss Lautet: {ergebniss}")