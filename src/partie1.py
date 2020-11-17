""" Partie 1 : Méthode incomplète de résolution """

from constantes import *
from API_liste_matrice import *

# renvoie T(j,l) (fonction inutile)
def ColorPoss(s,j,l):
    if (j < 0) or (l < 0):
        return False #élément neutre du ou
    elif (l == 0):
        return True
    elif (j == (s[1]-1)) and (l == 1):
        return True
    else:
        return ColorPoss(s,j-1,l) or ColorPoss(s,j-s[l]-1,l-1)

# Question 4 : construit le tableau T tel que T[j][l] = T(j,l) récursivement, en supposant que la grille est vide
# hypothèse : au début, j=M-1 et l=k
def ColoriagePossibleRec(T,s,j,l):
    if(T[j][l] != VIDE): #si on connaît déjà la valeur de T[j][l]
        return T[j][l]
    elif (j < 0) or (l < 0): #je le met car en python liste[-i] donne le i-ème élément de liste en partant de la fin, et nous on veut pas ça
        return False
    elif (l == 0): #cas de base 1
        T[j][l] = True
        return True
    elif (l == 1) and (j == s[0]-1): #cas de base de 2c
        T[j][l] = True
        return True
    if (j < s[l-1]-1): #cas de base 2a
        T[j][l] = False
        return False
    elif (j == s[l-1]-1): #cas de base 2b
        if (l == 1):
            T[j][l] = True
            return True
        else:
            T[j][l] = False
            return False
    else: #cas de base 2c
        T[j][l] = (ColoriagePossibleRec(T,s,j-1,l) or ColoriagePossibleRec(T,s,j-s[l-1]-1,l-1))
        return T[j][l]


# retourne False si v apparait dans une des cases du vecteur V entre les indices j1 et j2 inclus, True sinon
def TestVal(V,j1,j2,v):
    for i in range(j1,j2+1):
        if V[i] == v:
            return False
    return True

# Question 5 : construit le tableau T correspondant au vecteur V tel que T[j][l] = T(j,l) récursivement, sachant que certaines cases peuvent être déjà coloriées en blanc ou en noir
# hypothèse : au début, j=M-1 et l=k
def ColoriagePossibleRec2(V,s,j,l,T):
    if T[j][l] != VIDE:
        return T[j][l]
    elif l == 0: #cas de base 1
        T[j][l] = TestVal(V,0,j,NOIR)
        return T[j][l]
    elif (l == 1) and (j == s[l-1]-1): #cas de base de 2c
        T[j][l] = TestVal(V,0,j,BLANC)
        return T[j][l] 
    elif (j < 0) or (l < 0):
        return False
    elif j <= s[l-1]-1: #cas de base 2a
        T[j][l] = False
        return False
    elif T[j][l] == NOIR:
        b1 = False
    else:
        b1 = ColoriagePossibleRec2(V,s,j-1,l,T)
    
    if not TestVal(V,j-s[l-1]+1,j,BLANC):
        b2 = False
    elif V[j-s[l-1]] == NOIR:
        b2 = False
    else:
        b2 = ColoriagePossibleRec2(V,s,j-s[l-1]-1,l-1,T)
    
    # if b1 == True:      # en version if-else c'est ça non ? pourquoi ça marche pas ?
    #     T[j][l] = True  # dans tous les cas, la version b1 or b2 est mieux car c'est la relation de récurrence de 2c
    # elif b2 == True:
    #     T[j][l] == True
    # else:
    #     T[j][l] = False
    # # print(T[j][l])
    T[j][l] = (b1 or b2)
    return T[j][l]
        
    

# Question 9 : lecture du fichier
def lecture(filepath):
    retourligne = []
    retourcolonne = []
    with open(filepath,"r") as fp:
        contenu = " "
        colonne = False
        while contenu:
            contenu = fp.readline()
            if contenu:
                if (contenu == "#\n"):
                    colonne = True
                    continue
                if colonne :
                    x = []
                    courant = ""
                    for y in contenu:
                        if y == " ":
                            x.append(int(courant))
                            courant = ""
                        else:
                            if (y != "\n"):
                                courant = courant + y
                    if (courant != "") and (courant != "#"):
                        x.append(int(courant))
                    retourcolonne.append(x)
                    
                if (not(colonne)) :
                    x = []
                    courant = ""
                    for y in contenu:
                        if y == " ":
                            x.append(int(courant))
                            courant = ""
                        else:
                            if (y != "\n"):
                                courant = courant + y
                    if (courant != "") and (courant != "#"):
                        x.append(int(courant))
                    retourligne.append(x)
    #print(retourligne)
    #print(retourcolonne)
    return (retourligne,retourcolonne)

# colorie par récurrence un max de cases de la ligne i 
# TODO
def ColoreLig(G,i):
    return

# colorie par récurrence un max de cases de la colonne j
# TODO
def ColoreCol(G,j):
    return

# Algothme de coloration
def coloration(A):
    G = A   #copie de la grille
    N = len(G)  #nombre de lignes
    M = len(G[0])   #nombre de colonnes
    lignesAVoir = [i for i in range(N)]
    colonnesAVoir = [i for i in range(M)]

    while (lignesAVoir != []) or (colonnesAVoir != []):
        for i in lignesAVoir:
            (ok,G) = ColoreLig(G,i) #colorie par récurrence un max de cases de la ligne i ; ok = False si détection d'impossibilité, True sinon
            if not ok:
                return ("faux",init_matrice(M,0,VIDE))
            nouveaux = []   #numéro de colonne des nouvelles cases coloriées de la ligne i
            b = False
            for j in range(M):
                if G[i][j] != VIDE: #si la case (i,j) est coloriée
                    for k in colonnesAVoir: #on teste si j est déjà dans colonnesAVoir
                        if j == k:
                            b = True
                    if b == False:
                        nouveaux.append(j)
            colonnesAVoir = colonnesAVoir + nouveaux
            lignesAVoir = lignesAVoir.remove(i)
        
        for j in colonnesAVoir:
            (ok,G) = ColoreCol(G,j) #colorie par récurrence un max de cases de la colonne j ; ok = False si détection d'impossibilité, True sinon
            if not ok:
                return("faux",init_matrice(N,0,VIDE))
            nouveaux = []
            for i in range(N):
                if G[i][j] != VIDE: #si la case (i,j) est coloriée
                    for k in lignesAVoir: #on teste si j est déjà dans colonnesAVoir
                        if i == k:
                            b = True
                    if not b:
                        nouveaux.append(i)
            lignesAVoir = lignesAVoir + nouveaux
            colonnesAVoir = colonnesAVoir.remove(j)
        
        if matrice_coloriee(G): #si la matrice est entièrement coloriée
            return ("vrai",G)
        else:
            return ("neSaitPas",G)

# Question 9 : Algorithme de propagation
def propagation(filepath):
    s = lecture(filepath) #génération de la liste des séquences à partir du fichier texte
    A = init_matrice(len(s[0]),len(s[1]),VIDE) #initalisation grille de jeu

    (ok,G) = coloration(A)

    if ok == "vrai":
        print("La solution est :")
        affiche_matrice(G)
    elif ok == "faux":
        print("L'instance n'a pas de solution.")
    else:
        print("On ne peut pas conclure.")
    
