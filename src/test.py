""" Tests """

from constantes import *
from partie1 import *
from API_liste_matrice import  *
from partie2 import *
import time
# M = 9 #nombre de colonnes
# k = 3 #nombre de blocs noirs

# s = [1,3,2] #séquence

# # Ligne (commentaire =  relatif à l'algotithme de la question 5)
# L = [VIDE for i in range(M)] #donne un résultat correct
# L2 = [VIDE,VIDE,VIDE,VIDE,BLANC,VIDE,VIDE,VIDE,VIDE] #doit donner faux partout et c'est le cas
# L3 = [NOIR,BLANC,BLANC,NOIR,NOIR,NOIR,BLANC,NOIR,NOIR] #devrait donner le même résultat que pour L et c'est le cas
# L4 = [VIDE,BLANC,VIDE,NOIR,VIDE,VIDE,VIDE,VIDE,VIDE] #devrait donner le meme résultat que L et c'est le cas

# T = init_matrice(M,k+1,VIDE)

# # for j in range(len(T)): #Cas de base
# #     T[j][0] = True
# # T[s[0]-1][1] = True

# #ColoriagePossibleRec(T,s,M-1,k)
# ColoriagePossibleRec2(L3,s,M-1,k,T)

# affiche_matrice(T)


# Test lecture de fichier :
# filepath = "src/instances/0.txt"
# sequence = lecture(filepath)
# print(sequence)

#Test = lecture("./instances/0.txt")


#test2 = coloration(Test)

#print(test2[0])
#print("\n")
#affiche_matrice(test2[1][0])

'''N = 16
DictionnaireTemps = {}
for i in range(1,N):
    string = "./instances/"+str(i)+".txt"
    Test = lecture(string)
    start = time.perf_counter()
    test2 = Enumeration(Test)
    end = time.perf_counter()
    DictionnaireTemps[i] = (end-start)
    print("solution de l'instance "+str(i)+".txt")
    affiche_matrice(test2[1][0])
    if (i>11):
        test3 = coloration(Test)
        affiche_matrice(test3[1][0])

for i in range(1,N):
    print("l'instance "+str(i)+".txt a ete resolue en "+str(DictionnaireTemps[i])+" s")
'''

Test = lecture("./instances/13.txt")
test2 = Enumeration(Test)
affiche_matrice(test2[1][0])
