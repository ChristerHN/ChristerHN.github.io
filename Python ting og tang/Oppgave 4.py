#Dette programmet gjetter alderen din via random.randrage kommandoen.

import time
import random

navn = input("Hva heiter du?")
print("Hei", navn,"kan du sjå på kamera i 8 sekunder, imens jeg gjetter alderen din?")
alder = random.randrange(0,100)

time.sleep(8)

print("Ok,",navn,"det ser ut som du er", alder, "år gammel.")

rett = input("Er dette rett?")
print("Ingenting er perfekt, vet du.")

