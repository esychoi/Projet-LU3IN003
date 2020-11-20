""" Partie 1 : Méthode incomplète de résolution """

import copy

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
    if T[j][l] != VIDE: #si on a déjà calculé la valeur recherchée
        return T[j][l]
    elif l == 0: #cas de base 1
        T[j][l] = TestVal(V,0,j,NOIR)   #test s'il y a une case noire avant (i,j), auquel cas T(j,l)=faux puisqu'on est pas censé avoir de bloc noir du tout
        return T[j][l]
    elif (l == 1) and (j == s[0]-1): #cas de base de 2b
        T[j][l] = TestVal(V,0,j,BLANC)  #test s'il y a une case blanche avant (i,j), auquel cas T(j,l)=faux puisque les j+1 premières cases contiennet le bloc 1
        return T[j][l] 
    elif (j < 0) or (l < 0):    #je le met car en python liste[-i] donne le i-ème élément de liste en partant de la fin, et nous on veut pas ça
        return False
    elif j <= s[l-1]-1: #cas de base 2a et 2b pour l!=1
        T[j][l] = False
        return False
#A partir de là, on est dans le cas 2c j > s[l-1]-1

    #si (i,j) est blanche
    elif V[j] == NOIR:   #on ne peut pas avoir (i,j) noire
        b1 = False
    else:   #il faut tester si les l premiers blocs rentrent dans les j premières cases
        b1 = ColoriagePossibleRec2(V,s,j-1,l,T) 
    
    #si (i,j) est noire, alors (i,j) contient la dernière case du bloc l
    if not TestVal(V,j-s[l-1]+1,j,BLANC):   #teste s'il y a une case blanche entre (i,j-(s[l-1]-1)) et (i,j), c'est-à-dire tout le long du bloc l
        b2 = False  #car il ne doit pas y avoir de case blanche entre j-(s[l-1]-1) et j (puisqu'on est dans le bloc noir l)
    elif V[j-s[l-1]] == NOIR:   #si le test est vérifié, cela signifie que le bloc l se termine à la case (i,j-1) donc (i,j) ne pourrait être noire
        b2 = False
    else:   #il faut tester si les l-1 premiers blocs rentrent dans les j-(s[l-1]1) premières cases
        b2 = ColoriagePossibleRec2(V,s,j-s[l-1]-1,l-1,T)
    
    #si on ne sait pas la couleur de (i,j), alors on a calculé b1 et b2

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
    grille = init_matrice(len(retourligne),len(retourcolonne),VIDE)
    return (grille,retourligne,retourcolonne)

# colorie par récurrence un max de cases de la ligne i 
def ColoreLig(G,i,nouveaux): #on veut donc colorier V = G[0][i] avec la séquence s = G[1][i]
    V = copy.deepcopy(G[0][i])
    s = copy.deepcopy(G[1][i])
    M = len(V)
    j = M-1
    l = len(s)
    T = init_matrice(M,l+1,0)
    if not(ColoriagePossibleRec2(V,s,j,l,T)): #s'il n'y a pas de coloriage possible alors ce puzzle n'a pas de sol
        return (False,G)
    else:
        for k in range(0,M):#on parcourt les M cases de la i-eme ligne
            if V[k]==VIDE: #si on a pas encore colorié cette case
                T = init_matrice(M,l+1,0)
                V[k]=BLANC
                caseb = ColoriagePossibleRec2(V,s,j,l,T) #on test si la case peut etre coloriée en blanc
                T = init_matrice(M,l+1,0)
                V[k]=NOIR
                casen = ColoriagePossibleRec2(V,s,j,l,T) #on test si la case peut etre coloriée en noir
                if(caseb and casen): #si la case peut etre coloriee en noir ou blanc on ne peut rien en conclure donc on remet V[k] a VIDE
                    V[k] = VIDE 
                elif (caseb and not(casen)): #si la case peut etre blanche mais ne peut etre noire alors on la colorie en blanc
                    V[k] = BLANC
                    G[0][i][k] = BLANC
                    nouveaux.append(k)
                elif (casen and not(caseb)): #si la case peut etre noire mais ne peut etre blanche alors on la colorie en noir
                    V[k] = NOIR
                    G[0][i][k] = NOIR
                    nouveaux.append(k)
                elif (not(caseb) and not(casen)): #si la case ne peut etre coloriée alors le puzzle n'a pas de solution
                    return(False,G)
    return (True,G)


#transforme la j-ieme colonne en une ligne pour etre plus facile a traiter
def colonnetoligne(G,j):
    V=[]
    N = len(G[0])
    for k in range(0,N):
        V.append(G[0][k][j])
    return V

# colorie par récurrence un max de cases de la colonne j
def ColoreCol(G,j,nouveaux):
    V = colonnetoligne(G,j)
    s = copy.deepcopy(G[2][j])
    N = len(V)
    i = N-1
    l = len(s)
    T = init_matrice(N,l+1,0)
    if not(ColoriagePossibleRec2(V,s,i,l,T)):
        return (False,G)
    else:
        for k in range(0,N):
            if V[k]==VIDE:
                T = init_matrice(N,l+1,0)
                V[k]=BLANC
                caseb = ColoriagePossibleRec2(V,s,i,l,T)
                T = init_matrice(N,l+1,0)
                V[k]=NOIR
                casen = ColoriagePossibleRec2(V,s,i,l,T)
                if (casen and caseb):
                    V[k] = VIDE
                elif (caseb and not(casen)):
                    V[k] = BLANC
                    G[0][k][j] = BLANC
                    nouveaux.append(k)
                elif (casen and not(caseb)):
                    V[k] = NOIR
                    G[0][k][j] = NOIR
                    nouveaux.append(k)
                elif (not(caseb) and not(casen)):
                    return(False,G)
    return (True,G)


# Algothme de coloration
# TODO
def coloration(A):
    G = copy.deepcopy(A)   #copie de la grille
    N = len(G[0])  #nombre de lignes
    M = len(G[0][0])   #nombre de colonnes
    lignesAVoir = [i for i in range(N)]
    colonnesAVoir = [i for i in range(M)]

    while (lignesAVoir != []) or (colonnesAVoir != []):
        for i in lignesAVoir:
            nouveaux = []   #numéro de colonne des nouvelles cases coloriées de la ligne i
            (ok,G) = ColoreLig(G,i,nouveaux) #colorie par récurrence un max de cases de la ligne i ; ok = False si détection d'impossibilité, True sinon
            if not ok:
                return ("faux",init_matrice(M,0,VIDE))
            
            colonnesAVoir = colonnesAVoir + nouveaux
            lignesAVoir = [x for x in lignesAVoir if not(x==i)] 
        
        for j in colonnesAVoir:
            nouveaux = []
            (ok,G) = ColoreCol(G,j,nouveaux) #colorie par récurrence un max de cases de la colonne j ; ok = False si détection d'impossibilité, True sinon
            if not ok:
                return("faux",init_matrice(N,0,VIDE))
            
            lignesAVoir = lignesAVoir + nouveaux
            colonnesAVoir = [x for x in colonnesAVoir if not(x==j)]
        
    if matrice_coloriee(G[0]): #si la matrice est entièrement coloriée
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
        affiche_matrice(G[0])
    elif ok == "faux":
        print("L'instance n'a pas de solution.")
    else:
        print("On ne peut pas conclure.")
    