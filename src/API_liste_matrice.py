from constantes import *

# Crée et initalise toutes les cases de la matrice A de taille n*m à v
def init_matrice(n,m,v):
    return [[v for i in range(m)] for i in range(n)]

# Affiche la matrice A de taille n*m
def affiche_matrice(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if(A[i][j] == NOIR):
                print(u"\u25A0", end = '')
            elif(A[i][j] == BLANC):
                print(u"\u25A1", end = '' )

            else:
                print(A[i][j])
        print()
 

# Teste si la matrice G est entièrement coloriée
def matrice_coloriee(G):
    N = len(G)  #nombre de lignes
    M = len(G[0])   #nombre de colonnes

    for i in range(N):
        for j in range(M):
            if G[i][j] == VIDE:
                return False
    return True