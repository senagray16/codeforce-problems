t = int(input())

for _ in range(t):
    n = int(input())
    x = list(map(int,input().split()))
    x.sort()
    num = n
    li = [0]*n
    a = 0
    b = n-1
    lis = []
    for i in range(n):
        if i%2==0:
            li[a]=x[i]
            a +=1
        else:
            li[b]=x[i]
            b=b-1
        elem = x.count(x[i])
        if elem>2:
            if x[i] in lis:
                continue
            lis.append(x[i])
            num = num - (elem-2)
    print(num)
    j = ""
    for i in li:
        j += str(i) + " "
    print(j)