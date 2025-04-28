import os

path = os.path.join("./todo_list.txt")


exerciseList = []
marker = "x "
isRunning = True

def add_task():
    fileToWrite = open(path, "a+")
    exercise = input("Bitte gebe eine Aufgabe ein! ")
    try:
        fileToWrite.write(exercise + "\n")
    except Exception as error:
        print(error)
    finally:
        fileToWrite.close()

def readFile():
    fileToWrite = open(path, "r")
    exercises = []
    try:
        exercises = fileToWrite.readlines()
    except Exception as error:
        print(error)
    finally:
        fileToWrite.close()

    return exercises

def writeLinesToFile(data):
    fileToWrite = open(path, "w")

    try:
        fileToWrite.writelines(data)
    except Exception as error:
        print(error)
    finally:
        fileToWrite.close()

def show_task():
    exercises = readFile()

    i = 0
    listStrings = ""

    for exercise in exercises:
        listStrings += str(i) + f". {exercise}\n"
        i += 1;

    print(listStrings)

def mark_task_done():
    
    exercises = readFile()
    show_task()
    index = 0
    
    try:
        index = int(input("Bitte gebe eine Zahl ein: "))
    except:
        print("Bitte gebe NUR eine Zahl ein! ")
        mark_task_done()

    exercises[index] = marker + exercises[index]

    writeLinesToFile(exercises)


def delete_task():
    
    exercises = readFile()
    show_task()
    index = 0

    try:
        index = int(input("Bitte gebe eine Zahl ein: "))
    except:
        print("Bitte gebe NUR eine Zahl ein! ")
        delete_task()

    del exercises[index]

    writeLinesToFile(exercises)

while isRunning:
    print("""1. Aufgabe hinzufügen
2. Aufgaben anzeigen
3. Aufgabe als erledigt markieren
4. Aufgabe löschen
5. Beenden
""")


    index = int(input("Bitte gebe eine Zahle ein: "))
    if(index == 5):
        isRunning = False
    elif(index == 1):
        add_task()
    elif(index == 2):
        show_task()
    elif(index == 3):
        mark_task_done()
    elif(index == 4):
        delete_task()


