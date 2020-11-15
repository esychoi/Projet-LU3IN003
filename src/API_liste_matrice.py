#crée et initalise toutes les cases de la matrice A de taille n*m à v
def init_matrice(n,m,v):
    return [[v for i in range(m)] for i in range(n)]

#affiche la matrice A de taille n*m
def affiche_matrice(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end = ' ')
        print()