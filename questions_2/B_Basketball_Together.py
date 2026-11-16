n, k = map(int,input().split())

x = list(map(int,input().split()))
x.sort()
i = 0
j = n-1

total = x[j]
maxu = x[j]
ans = 0
while(i<=j):
    if total>k:
        ans +=1
        j -=1
        total=x[j]
        maxu = x[j]
    else:
        total += maxu
        i +=1
print(ans)
