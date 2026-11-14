t= int(input())

for _ in range(t):
    n = int(input())
    x = list(map(int,input().split()))


    for i in range(1,n):
        if x[i]<x[i-1]:
            x[i],x[i-1]=x[i-1],x[i]
            x[i] +=x[i-1]
    print(x[-1])