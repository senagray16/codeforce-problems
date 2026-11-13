t = int(input())

for _ in range(t):
    n,l,r = list(map(int,input().split()))
    a = list(map(int,input().split()))

    div = {}
    for i in range(n):
        div[a[i]]=i

    a.sort()
    i = 0
    j = n-1
    num = 0
    while(j>i):
        if a[i]+a[j]>=l and a[i]+a[j]<=r:
            num +=1
            i = i +1
            j -= 1
        elif a[i]+a[j]<l:
            i +=1
        else:
            j -=1
    print(num* num)