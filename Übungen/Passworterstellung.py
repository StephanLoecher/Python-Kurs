password = input("Passwort eingeben: ")
minLength = 8
isPasswordMinLength = False
containsNumber = False
containsSpecialChar = False

if password.__len__() >= minLength:
    isPasswordMinLength = True

for char in password:
    if char.isnumeric():
        print("True")
        break

for char in password:
    if not char.isalnum():
        containsSpecialChar = True
        break
if isPasswordMinLength and containsNumber and containsSpecialChar:
    print("Password is safe")
else:
    print("Password is not safe")

