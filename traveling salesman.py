from math import inf
from math import sqrt

def d(C,i,j):
    return sqrt((C[i][1]-C[j][1])**2+(C[i][2]-C[j][2])**2)

def smallest(C):
    small=inf
    index=0
    for i in range(len(C)):
        if C[i][1]<small:
            index=i
            small=C[i][1]
    return index

def largest(C):
    large=-inf
    index=0
    for i in range(len(C)):
        if C[i][1]>large:
            index=i
            large=C[i][1]
    return index


def tspf(i,j,F,D):
    if F[i][j]!=inf:
        return F[i][j]
    if i==j-1:
        best=inf
        for k in range(j-1):
            best=min(best,tspf(k,j-1,F,D)+D[k][j])
        F[j-1][j]=best
    else:
        F[i][j]=tspf(i,j-1,F,D)+D[j-1][j]
    return F[i][j]

C = [["Wrocław", 0, 2], ["Warszawa",4,3], ["Gdańsk", 2,4], ["Kraków",3,1]]
n=4 #ilość miast
D=[[d(C,i,j)for i in range(n)]for j in range(n)]
F=[[inf]*n for i in range(n)]
F[0][1]=D[0][1]
F[1][0]=D[1][0]
print(tspf(smallest(C),largest(C),F,D)+d(C,smallest(C),largest(C)))
