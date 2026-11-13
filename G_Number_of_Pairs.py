t = int(input())

for _ in range(t):
    n,l,r = list(map(int,input().split()))
    a = list(map(int,input().split()))

    a.sort()
    i = 0
    j = n-1
    num = 0
    while(j>i):
        if a[i]+a[j]<l:
            num +=j-i
            i = i +1
        else:
            j = j-1
    i = 0
    j = n-1
    num2 = 0
    while(j>i):
            if a[i]+a[j]<=r:
                num2 +=j-i
                i = i +1
            else:
                j = j-1
    print(num2-num)