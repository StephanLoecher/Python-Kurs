# Nehme einen Input gegen
# Prüfe den Input ob es eine Zahl ist, wenn ja gebe sie , wenn nein wandle sie um und gebe sie aus


Eingabe = input("Gebe bitte etwas ein: ")

try:
    if "." in Eingabe:
        print(f"Line 9 {float(Eingabe)}")
    else:
        print(f"Line 11 {int(Eingabe)}")
except:
    print("Die Eingabe war keine Zahl")
