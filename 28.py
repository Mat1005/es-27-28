''' 
I CAP vengono inseriti e memorizzati in un dizionario.
Fornito poi il nome della città crea un programma che visualizzi il suo CAP e viceversa.
'''
CAP_dizionario = {}
Città_dizionario = {}
tot = int(input())
While True:
    nome_città = ("Inserire il nome della città")
    CAP = int(input("Inserire il CAP"))
    CAP_dizionario[CAP] = nome_città
