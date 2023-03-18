def knapsack (W,P,maxP,maxW):
    n=len(W)


    F = [[0 for i in range(maxP+1)] for j in range(n)]

    for i in range(n):
        F[i][P[i]]=W[i]

    for i in range(1,n):
        for p in range(1,maxP+1):
            if F[i-1][p]!=0:
                F[i][p+P[i]]=F[i-1][p]+W[i]
            if F[i-1][p]!=0 and (F[i][p]==0 or F[i-1][p]<F[i][p]):
                F[i][p]=F[i-1][p]



    i=maxP
    while i>=0:
        if F[n-1][i]<=maxW:
            return  i, F
        i-=1


def getSolution(F,P,i,p):#i=n-1 p=maxP, w=maxW
    if i==0:
        if F[i][p]!=0: return [0]
        else: return []
    if F[i-1][p]!=F[i][p]:
        return getSolution(F,P,i-1,p-P[i])+[i]
    return getSolution(F, P, i - 1,p)

W=[10,14,5,5]
P=[1,2,8,1]

maxP = 0
for i in range(len(P)): maxP += P[i]

index=knapsack(W,P,maxP, 10)[0]
tab=knapsack(W,P,maxP, 10)[1]

print(getSolution(tab,P,len(P)-1,index))
#print(knapsack(W,P,maxP, 10))
