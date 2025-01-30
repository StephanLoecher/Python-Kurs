#programmiert mit Copilot
# Definiere die Funktionen für die Grundrechenarten
def addiere(x, y):
    return x + y

def subtrahiere(x, y):
    return x - y

def multipliziere(x, y):
    return x * y

def dividiere(x, y):
    if y != 0:
        return x / y
    else:
        return "Teilung durch Null ist nicht erlaubt!"

# Hauptprogramm
def taschenrechner():
    print("Wähle die Operation:")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")

    auswahl = input("Gib deine Wahl ein (1/2/3/4): ")

    num1 = float(input("Gib die erste Zahl ein: "))
    num2 = float(input("Gib die zweite Zahl ein: "))

    if auswahl == '1':
        print("Ergebnis:", addiere(num1, num2))
    elif auswahl == '2':
        print("Ergebnis:", subtrahiere(num1, num2))
    elif auswahl == '3':
        print("Ergebnis:", multipliziere(num1, num2))
    elif auswahl == '4':
        print("Ergebnis:", dividiere(num1, num2))
    else:
        print("Ungültige Auswahl")

# Starte den Taschenrechner
taschenrechner()
