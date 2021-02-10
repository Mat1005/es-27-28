'''
Organizza con un dizionario la rubrica telefonica.
Fornito poi il numero della persona visualizzare poi il numero o inviare un messaggio in caso non sia presente nella lista.

'''
rubrica = {"Matteo Zaccarelli":"366 042 8604",
"Simone Melli":"333 184 0037",
"Enrico Rossi":"355 536 2242",
"Riccardo Malavasi":"367 264 1131",
"Giorgio Bondavalli":"354 242 4523",
"Marco Antonio":"346 252 5563",
"Luca Bianchi":"353 942 4324"}
nome = input("Di chi vuoi sapere il numero?")
if nome in rubrica:
    print("Il numero del contatto ",nome," è:",rubrica[nome])
else:
    print("Il contatto ",nome," non è in rubrica.")
