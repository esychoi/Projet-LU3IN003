from partie1 import *

def colorieretpropager(A,i,j,c):
    G = copy.deepcopy(A)   #copie de la grille
    G[0][i][j] = c
    N = len(G[0])  #nombre de lignes
    M = len(G[0][0])   #nombre de colonnes
    lignesAVoir = [i]
    colonnesAVoir = [j]

    while (lignesAVoir != []) or (colonnesAVoir != []):
        for i in lignesAVoir:
            nouveaux = []   #numéro de colonne des nouvelles cases coloriées de la ligne i
            (ok,G) = ColoreLig(G,i,nouveaux) #colorie par récurrence un max de cases de la ligne i ; ok = False si détection d'impossibilité, True sinon
            if not ok:
                return ("faux",init_matrice(M,0,VIDE))
            
            colonnesAVoir.extend(x for x in nouveaux if x not in colonnesAVoir)
            lignesAVoir = [x for x in lignesAVoir if not(x==i)]
        
        for j in colonnesAVoir:
            nouveaux = []
            (ok,G) = ColoreCol(G,j,nouveaux) #colorie par récurrence un max de cases de la colonne j ; ok = False si détection d'impossibilité, True sinon
            if not ok:
                return("faux",init_matrice(N,0,VIDE))
            
            lignesAVoir.extend(x for x in nouveaux if x not in lignesAVoir)
            colonnesAVoir = [x for x in colonnesAVoir if not(x==j)]
        
    if matrice_coloriee(G[0]): #si la matrice est entièrement coloriée
        return ("vrai",G)
    else:
        return ("neSaitPas",G)

  


def trouvek(A,i,j,M,N):
    for i2 in range(i,N):
        for j2 in range(j,M):
            if (A[0][i2][j2] == VIDE):
                return M*i2+j2
    return M*N

def enum_rec(A,k,c):
    
    N = len(A[0])  #nombre de lignes
    M = len(A[0][0])   #nombre de colonnes
    
    if (k==M*N):
        return True
    i = k // M
    j = k % M

    (ok,A0) = colorieretpropager(A,i,j,c)

    if (ok == "faux"):
        return(False,A0)
    if (ok == "vrai"):
        return(True,A0)

    k1 = trouvek(A0,i,j,M,N)

    (ok,A1) = enum_rec(A0,k1,BLANC)
    if ok:
        return (ok,A1)
    
    else:
        (ok,A1) = enum_rec(A0,k1,NOIR)
        if ok:
            return (ok,A1)
    return (False,A)

def Enumeration(A):
    (ok,A0) = coloration(A)
    if(ok=="faux"):
        return (False,A0)
    elif(ok=="vrai"):
        return (True,A0)

    k = trouvek(A0,0,0,len(A[0][0]),len(A[0])) #on colorie la premiere case non coloriée
    
    (ok1,A1) = enum_rec(A0,k,BLANC)
    if (ok1):
        return (ok1,A1)
    else:
        (ok2,A2) = enum_rec(A0,k,NOIR)
        if(ok2):
            return (ok2,A2)
    return (False,A)