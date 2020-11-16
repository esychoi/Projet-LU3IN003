from partie1 import *
from API_liste_matrice import  *

# VARIABLES GLOBALES (euh en fait ça marche pas mais je suis sure qu'il y a un équivalent du #define de C en Python)
vide = -1
blanc = 0
noir = 1

M = 9 #nombre de colonnes
k = 3 #nombre de blocs noirs

s = [1,3,2] #séquence

# Ligne (commentaire =  relatif à l'algotithme de la question 5)
L = [vide for i in range(M)] #donne un résultat correct mais pas le même que la fonction de la question 4 (jsp si c'est normal)
L2 = [vide,vide,vide,vide,blanc,vide,vide,vide,vide] #doit donner faux partout et c'est le cas
L3 = [noir,blanc,blanc,noir,noir,noir,blanc,noir,noir] #devrait donner le même résultat que pour L mais ça met T[7][2] = False alors que c'est True nan ?
L4 = [vide,blanc,vide,noir,vide,vide,vide,vide,vide] #devrait donner le meme résultat que L et c'est le cas

T = init_matrice(M,k+1,vide)

# for j in range(len(T)): #Cas de base
#     T[j][0] = True
# T[s[0]-1][1] = True

# ColoriagePossibleRec(T,s,M-1,k)
ColoriagePossibleRec2(L4,s,M-1,k,T)

affiche_matrice(T)


# Test lecture de fichier :
# filepath = "src/instances/0.txt"
# sequence = lecture(filepath)
# print(sequence)