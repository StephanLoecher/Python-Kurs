liste = [1500, 1000, 500, 4000, 3000, 200]
bezahlbare = []
for i in liste:
    if i <= 1000:
        bezahlbare.append(i)
    else:
        print(str(i) + " ist zu teuer!")
print(bezahlbare)