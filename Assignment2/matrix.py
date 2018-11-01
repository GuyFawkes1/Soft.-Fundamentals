N = 200
from random import randint

lista  = [[-1 for i in range(0,N)] for j in range(0,N)]
for i in range(0,N):
    for j in range(i,N):
        if (i==j):
            lista[i][j]=0
        
        else:
            lista[i][j] = randint(0,1)
            #lista[i][j] = 1
            lista[j][i] = lista[i][j] 

for i in range(0,N):
    for j in range(0,N):
        print(lista[i][j],end=' ')
    print()