def return1(x):
    if x < 10:
        return True
    
    return False

var1 = return1(5)

print(var1)

if return1(11):
    print("1 is lower")


prices = [2,6,25,235,1]

def calculate(priceList):
    gesamtPreis = 0

    for preis in priceList:
        gesamtPreis += preis
    
    return gesamtPreis

print(calculate(prices))




# Schreibt eine Funktion
# mit einem If statement
# if age < 18 geb zurück "Du bist nicht alt genug"
# if age == 18 geb zurück "Du bist gerade alt genug"
# if age > 18 geb zurück "Du bist alt genug"
# print den zurück gegebenen string
