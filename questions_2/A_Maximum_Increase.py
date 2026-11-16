n = int(input())
x = list(map(int,input().split()))

a = 1
maxa = 0
i = 0
j = 1
while(j<n):
    if x[i]<x[j]:
        a +=1
        i +=1
        j +=1
    else:
        if a>maxa:
            maxa = a
        a = 1
        i +=1
        j +=1
if a>maxa:
    maxa =a
        
print(maxa)