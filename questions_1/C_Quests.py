t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    aa = list(map(int,input().split()))
    bb = list(map(int,input().split()))

    open = 0
    sum = 0
    for i in range(k):
        if open==n:
            a = max(bb)
            sum += a
        elif i==0:
            sum += aa[open]
            open +=1
        else:
            a = max(bb[:open])
            if a>aa[open]:
                sum += a
            else:
                sum += aa[open]
                open +=1

    print(sum)