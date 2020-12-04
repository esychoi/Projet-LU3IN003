from constantes import *
from partie1 import *
from API_liste_matrice import  *
from partie2 import *
import time

N = 17 #nombre d'instances

# Algorithme de coloration
print("ALGORITHME DE COLORATION")
DictionnaireTemps = {}
for i in range(1,N):
    string = "src/instances/"+str(i)+".txt"
    seq = lecture(string)
    start = time.perf_counter()
    test2 = coloration(seq)
    end = time.perf_counter()
    DictionnaireTemps[i] = (end-start)
    print("solution de l'instance "+str(i)+".txt :")
    affiche_matrice(test2[1][0])

for i in range(1,N):
    print("l'instance "+str(i)+".txt a été résolue en "+str(DictionnaireTemps[i])+" s avec l'algorithme de coloration")

# Algorithme d'énumération
print("ALGORITHME D'ENUMERATION")
DictionnaireTemps = {}
for i in range(1,N):
    string = "src/instances/"+str(i)+".txt"
    seq = lecture(string)
    start = time.perf_counter()
    test2 = Enumeration(seq)
    end = time.perf_counter()
    DictionnaireTemps[i] = (end-start)
    print("solution de l'instance "+str(i)+".txt :")
    affiche_matrice(test2[1][0])

for i in range(1,N):
    print("l'instance "+str(i)+".txt a été résolue en "+str(DictionnaireTemps[i])+" s avec l'algorithme d'énumération'")