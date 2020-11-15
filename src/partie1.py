""" Partie 1.1 : Première partie """

#renvoie T(j,l)
def ColorPoss(s,j,l):
    if (j < 0) or (l < 0):
        return False #élément neutre du ou
    elif (l == 0):
        return True
    elif (j == (s[1]-1)) and (l == 1):
        return True
    else:
        return ColorPoss(s,j-1,l) or ColorPoss(s,j-s[l]-1,l-1)

#construit le tableau T tel que T[j][l] = T(j,l) récursivement
#hypothèse : au début, j=M-1 et l=k
def ColoriagePossibleRec(T,s,j,l):
    if (j < 0) or (l < 0):
        return False
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
        if (T[j-1][l] != -1) and (T[j-s[l-1]-1][l-1] != -1):
            T[j][l] = (T[j-1][l] or T[j-s[l-1]-1][l-1])
            return T[j][l]
        elif (T[j-1][l] != -1):
            T[j][l] = ((T[j-1][l]) or ColoriagePossibleRec(T,s,j-s[l-1]-1,l-1))
            return T[j][l]
        elif (T[j-s[l-1]-1][l-1] != -1):
            T[j][l] = (ColoriagePossibleRec(T,s,j-1,l) or T[j-s[l-1]-1][l-1])
            return T[j][l]
        else:
            T[j][l] = (ColoriagePossibleRec(T,s,j-1,l) or ColoriagePossibleRec(T,s,j-s[l-1]-1,l-1))
            return T[j][l]

