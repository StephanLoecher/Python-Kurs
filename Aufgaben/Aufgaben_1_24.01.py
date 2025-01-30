# Erstelle 8 Variablen mit je einem anderen Datentyp
# Funktion int
def ganzeZahlen(num1: int):
    print(f"Line 4: Ganze Zahl: {num1}")
    return num1

# Funktion float
def Kommazahlen(num2: float):
    print(f"Line 9: Kommazahl: {num2}")
    return num2

# Funktion str
def zeichenketten(text: str):
    print(f"Line 14: Zeichenkette: {text}")
    return text

# Funktion bool
def boolen(true: bool):
    print(f"Line 19: Boolen: {true}")
    return true

# Funktion list
def listen(liste: list):
    print(f"Line 24: Liste: {liste}")
    return liste

# Funktion tuple
def tupel(tup: tuple):
    print(f"Line 29: Tupel: {tup}")
    return tup

# Funktion set
def mengen(menge: set):
    print(f"Line 34: Menge: {menge}")
    return menge

# Funktion dict
def woerterbuecher(wörterbuch: dict):
    print(f"Line 39: Wörterbuch: {wörterbuch}")
    return wörterbuch

# Beispiel Funktionen
# Benenne die Datentypen der Variablen
ganzeZahlen = (5)  # Int
Kommazahlen = (5.555)  # Float
zeichenketten = ("Hallo, Welt!")  # Str
boolen = (True)  # Bool
listen = [1, 2, 3, 4, 5]  # List
tupel = (1, "zwei", 3.0)  # Tuple
mengen = {1, 2, 3, 4, 5}  # Set
woerterbuecher = {"Name": "Alice", "Alter": 30}  # Dict

# Nehme einen Input entgegen und speichere ihn in die Variable ab
test = input("Line 54: Test Bitte gebe was ein um den Typen zu bestimmen: ")

def iAmAnotherDefinition(test):
    if not test.isalnum():
        print(f"Die Eingabe: {test} enthält Sonderzeichen und ist ungültig.")
        return
    
    try:
        int_test = int(test)
        print(f"Die Eingabe: {int_test} ist ein Integer")
    except:
        try:
            float_test = float(test)
            print(f"Die Eingabe: {float_test} ist ein Float")
        except:
            print(f"Die Eingabe: {test} ist ein String")
            
iAmAnotherDefinition(test)
# Schreibe eine Methode
# Nehme in der Methode 2 Parameter entgegen.      
# Schreibe eine beliebige funktionierende Logik mit folgendem Inhalt:
# - es muss ein if statement drin sein
# - es muss eine for loop enthalten sein
# - es muss ein logischer Operator enthalten sein

def Bsp(x, y):
    if x == y:
        print(f"Line 80: x ist gleich y")

    if y >= x:
        print("Line 84: y ist größer als x")
    elif y == x:
        print("Line 86: y ist gleich x")
    else:
        print("Line 88: y ist kleiner als x")

    for i in range(5):
        print("Line 92: Zahl:", i + i)

# Führe die Methode Bsp aus
Bsp(2, 2)
