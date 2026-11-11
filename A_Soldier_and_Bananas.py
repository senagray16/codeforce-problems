k,w,n = list(map(int,input().split()))

sum = 0
for i in range(n):
    sum += i+1

costw = sum*k
if costw>w:
    print(costw-w)
else:
    print(0)