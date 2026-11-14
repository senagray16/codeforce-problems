t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()

    i = 0
    j = n-1
    score = 0
    while(j>i):
        if x[i]+x[j]==k:
            score +=1
            j = j - 1
            i = i + 1
        elif x[i]+x[j]>k:
            j = j - 1
        else:
            i = i + 1
    print(score)
