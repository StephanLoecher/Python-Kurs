import os
from model import softwareNames


def installSoftware(zahlTuple):
  
    for zahl in zahlTuple:

        name = softwareNames.softwareNames[int(zahl)]
        os.system(f"sudo apt get install {name} -y" )
    
        print(f"{name} wurde jetzt installiert")

