from partie1 import *
from API_liste_matrice import  *

M = 9
k = 3

s = [1,3,2] #séquence

T = init_matrice(M,k+1,-1)

for j in range(len(T)): #Cas de base
    T[j][0] = True
T[s[0]-1][1] = True
ColoriagePossibleRec(T,s,M-1,k)
affiche_matrice(T)
