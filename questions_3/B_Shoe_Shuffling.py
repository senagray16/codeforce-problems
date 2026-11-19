t = int(input())

for _ in range(t):
    n = int(input())
    x = list(map(int,input().split()))

    a = 0
    start = 0
    end = 0
    last = x[0]
    dili = []
    for i in x:
        if x.count(i)==1:
            a = 1
            break
        
        if last == i:
            end+=1
        else:
            last = i
            dili.append((start,end))
            start = end
    print(dili)


    if a==1:
        print("-1")
    else:
        print()
