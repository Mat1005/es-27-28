''' 
I CAP vengono inseriti e memorizzati in un dizionario.
Fornito poi il nome della città crea un programma che visualizzi il suo CAP e viceversa.
'''
CAP_dizionario = {}
Citta_dizionario = {}
tot = int(input("Quante sono le città?"))
for n in range (1, tot + 1):
    nome_citta = input("Inserire il nome della città")
    CAP = int(input("Inserire il CAP"))
    CAP_dizionario[CAP] = nome_citta
    Citta_dizionario[nome_citta] = CAP
citta = input("Di quale città vuoi sapere il CAP ?")
if citta in Citta_dizionario:
    print("Il Cap di ",citta," è:",Citta_dizionario[citta])
else:
    print("La città",citta," non è nella lista.")
cap = int(input("Inserire il CAP di cui vuoi conoscere la città "))
if cap in CAP_dizionario:
    print("Il CAP ",cap," è della città di ",CAP_dizionario[cap])
else:
    print("Il CAP ",cap," non è nella lista.")
   
