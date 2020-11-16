""" Partie 1 : Méthode incomplète de résolution """
vide = -1
blanc = 0
noir = 1

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
    global vide

    if(T[j][l] != vide): #si on connaît déjà la valeur de T[j][l]
        return T[j][l]
    elif (j < 0) or (l < 0): #je le met car en python liste[-i] donne le i-ème élément de liste en partant de la fin, et nous on veut pas ça
        return False
    elif (l == 0): #cas de base 1
        T[j][l] = True
        return True
    elif (j == s[l-1]-1) and (l == 1): #cas de base de 2c
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


# retourne False si v apparait dans une des cases d'une ligne entre les indices j1 et j2 inclus, True sinon
def TestVal(L,j1,j2,v):
    for i in range(j1,j2+1):
        if L[i] == v:
            return False
    return True

# Question 5 : construit le tableau T tel que T[j][l] = T(j,l) récursivement, sachant que certaines cases peuvent être déjà coloriées en blanc ou en noir
# hypothèse : au début, j=M-1 et l=k
def ColoriagePossibleRec2(L,s,j,l,T):
    global vide
    global noir
    global blanc

    if T[j][l] != vide:
        return T[j][l]
    elif l == 0: #cas de base 1
        return TestVal(L,0,j,noir)
    elif (l == 1) and (j == s[l-1]-1): #cas de base
        return TestVal(L,0,j,blanc)
    elif (j < 0) or (l < 0):
        return False
    elif j <= s[l-1]-1: #cas de base 2a
        return False
    elif T[j][l] == noir:
        b1 = False
    else:
        b1 = ColoriagePossibleRec2(L,s,j-1,l,T)
    
    if not TestVal(L,j-s[l-1]+1,j,blanc):
        b2 = False
    elif L[j-s[l-1]] == noir:
        b2 = False
    else:
        b2 = ColoriagePossibleRec2(L,s,j-s[l-1]-1,l-1,T)
    
    # if b1 == True:      # en version if-else c'est ça non ? pourquoi ça marche pas ?
    #     T[j][l] = True  # dans tous les cas, la version b1 or b2 est mieux car c'est la relation de récurrence de 2c
    # elif b2 == True:
    #     T[j][l] == True
    # else:
    #     T[j][l] = False
    # # print(T[j][l])
    T[j][l] = (b1 or b2)
    # print(T[j][l])
    return T[j][l]
        
    

# lecture du fichier
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