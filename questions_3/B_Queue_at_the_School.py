n, k = map(int,input().split())

x = input()


if n==1:
    print(x)
else:
    for i in range(k):
        x = list(x)
        i = 0
        j = 1
        while(j<n):
            if x[i]=="B" and x[j]=="G":
                x[i],x[j]=x[j],x[i]
                i = j + 1
                j = j + 2
            else:
                i = i +1
                j = j +1
    print("".join(x))
