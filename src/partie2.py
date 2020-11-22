from partie1 import *

def colorieretpropager(A,i,j,c):
    return

def trouvek(A,i,j,M,N):
    for i2 in range(i,N):
        for j2 in range(j,M):
            if (A0[0][i2][j2] == VIDE):
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

    if (ok == False):
        return(False,A0)
    if (ok):
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
    (ok1,A1) = enum_rec(A0,0,BLANC)
    if (ok1):
        return (ok1,A1)
    else:
        (ok2,A2) = enum_rec(A0,0,NOIR)
        if(ok2):
            return (ok2,A2)
    return (False,A)