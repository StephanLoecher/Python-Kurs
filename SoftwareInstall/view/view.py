from controller import installController
from model import softwareNames

def Start():
    getSoftwareNumber()


def getSoftwareNumber():

    nameList : str = ""
    index : int = 0

    choices = ""
    choicesTuple = ""

    for software in softwareNames.softwareNames:
        nameList += ( str(index) + f" {software}\n")
        index += 1

    try:
        choices = input(f"""Please choose numbers seperated with , :
{nameList}
""")
        choicesTuple = tuple(choices.strip().split(","))    
        installController.installSoftware(choicesTuple)
        print("Software modules successfully installed.")
    except:
        print("Please choose a number only and seperat it with a , !")
        getSoftwareNumber()

