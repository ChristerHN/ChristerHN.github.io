#dette programmet skal lage ett visitkort til deg med hjelp av info som du gir den

import time

navn = input("Hva er namnet ditt?")
adresse = input("Hva er adressen din?")
postnummer = input("Hva er postnummeret ditt?")
stad = input("Hvor er du fra?")

print("Takk, vent 5 sekund no")

time.sleep(5)

print("""


--------------""")
print(navn)
print(adresse)
print(postnummer)
print(stad)
print("-------------")