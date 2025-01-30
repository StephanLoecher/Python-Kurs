x = 3
y = 25

s = 23

def printMessage(line):
    print(f"Do something: Line: {line}")

if x < y or x == s:
    printMessage(11)

if x < y and x == s:
    printMessage(14)

if x < y is not x == s:
    printMessage(17)

if x < y is x == s:
    printMessage(20)

