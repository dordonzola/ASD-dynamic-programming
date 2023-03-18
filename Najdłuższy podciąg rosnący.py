#Dynamicznie znajduje długość najdłuższego podciągu spójnego
def LIS(A):
    n=len(A)
    F=[1]*n
    P=[-1]*n
    for i in range(1,n):
        for j in range(i):
            if A[j]<A[i] and F[i]<F[j]+1:
                F[i]=F[j]+1
                P[i]=j

    for i in range(n):
        if F[i]==max(F):
            index=i
            break

    return max(F),index, P

def printAllLIS(A,P,i):
    if P[i]>=0:
        printAllLIS(A,P,P[i])
    print(A[i])

A=[3,1,5,7,2,4,9,3,17,3]

P=LIS(A)[2]
i=LIS(A)[1]

printAllLIS(A,P,i)