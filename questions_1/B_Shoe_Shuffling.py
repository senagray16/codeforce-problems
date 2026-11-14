t = int(input())

for _ in range(t):
    n = int(input())

    x = list(map(int,input().split()))
    a = 0
    b =""
    for i in x:
        if x.count(i)>1:
            a =1 
            b = i
            break
    if a==0:
        print("-1")
    else:
        a = x.index()
        print(a)
    