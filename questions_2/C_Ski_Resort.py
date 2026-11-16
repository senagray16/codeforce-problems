t = int(input())

for _ in range(t):
    n,k,m = list(map(int,input().split()))
    x = list(map(int,input().split()))

    i = 0
    j = []
    for a in x:
        if a<=m:
            i +=1
        else:
            if i!=0:
                j.append(i)
            i = 0
    if len(j)==0 and i==0:
        print(0)
        continue

    j.append(i)
    suma = 0
    
    for a in j:
        suma += ((a-k+1)*(a-k+2))//2

    print(suma)