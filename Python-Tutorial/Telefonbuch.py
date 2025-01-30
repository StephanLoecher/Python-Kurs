telefonbuch = {
    "Ali": "0163637833",
    "Mohammed": "015736244",
    "Othman": "0177653343",
    "Ahmad": "015837363",
}
a = input("Welche Telefonnummer brauchst du? ")
if a in telefonbuch:
    print (a, "Nummer ist", telefonbuch["Ahmad"])
else:
    print(a, "Ist nicht in unserem Telefonbuch")