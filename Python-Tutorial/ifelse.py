""""
streckeinkm = 3

if streckeinkm > 3:
    print("Lauf doch zu Fuß!")
elif streckeinkm == 3:
    print("Ganz schön lange Strecke!")
else:
    print("Nimm doch hier das Fahrrad!")
"""


alter = int(input("Geben Sie ihr Alter ein: "))
anzahl = int(input("Wie viele Tickets nehmen Sie?"))

if alter > 65:
    print(7.5 * anzahl)
elif alter >= 18:
    print(10 * anzahl)
else:
    print(5 * anzahl)
