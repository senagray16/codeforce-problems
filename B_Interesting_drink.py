n = int(input())

x = list(map(int,input().split()))
x.sort()

q = int(input())
li = []
for _ in range(q):
    y = int(input())
    i = 0
    j = n -1
    ans = -1
    while (i<=j):
        mid = (i+j)//2
        if x[mid]>y:
            j = mid-1
        else:
            ans = mid
            i = mid+1
    print(ans+1)







