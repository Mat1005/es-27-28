''' 
I CAP vengono inseriti e memorizzati in un dizionario.
Fornito poi il nome della città crea un programma che visualizzi il suo CAP e viceversa.
'''
CAP_dizionario = {}
Citta_dizionario = {}
tot = int(input())
for n in range (1, tot + 1):
    nome_citta = ("Inserire il nome della città")
    CAP = int(input("Inserire il CAP"))
    CAP_dizionario[CAP] = nome_citta
    Citta_dizionario[nome_citta] = CAP
