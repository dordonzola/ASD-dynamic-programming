#Dynamicznie znajduje długość najdłuższego podciągu sumującego się do T

def T_sum(A,T):
    n=len(A)
    F=[[0 for i in range(T+1)] for j in range(n)]

    for i in range(n):
        if A[i]==T: return True
        if A[i]<T:
            for j in range(T):
                if j==A[i]: F[i][j]=A[i]

    for i in range(1,n):
        for j in range(1,T):
            if F[i - 1][j] != 0 and j + A[i]<=T:
                F[i][j + A[i]] = F[i - 1][j] + i
            if F[i - 1][j] != 0 and F[i][j] == 0:
                F[i][j] = F[i - 1][j]

    if F[n-1][T]!=0: return True
    return False



