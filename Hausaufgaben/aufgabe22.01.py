#Erstellt einen Liste mit städtenamen
#Sortiert diese Liste

Staedte = ["München", "Köln", "Berlin", "Frankfurt", "Hamburg", "Stuttgart"]
Staedte.sort()
print(Staedte)

#checkt mit contains ob 2 städte enthalten sind
#gebt diese städte ins terminal aus

Stadt1 = "Köln"
Stadt2 = "München"
if Staedte.__contains__(Stadt1) and Staedte.__contains__(Stadt2):
    print("2 Städte gefunden: ")
    print(f'{Stadt1}, {Stadt2}')

 
#Macht ein tupel mit vornamen
#macht ein tupel mit nachnamen
#verbidnet vor und nachname für die email mit einem punkt (join methode)

vornamen = ("John", "Max", "Tom", "Gustavo")
nachnamen = ("Black", "Lee", "Johnson", "Parker")

domain = "@skyered.de"
i = 0
for namen in vornamen:
    name = ".".join([vornamen[i], nachnamen[i]])
    name += domain
    print(name)
    i +=1
