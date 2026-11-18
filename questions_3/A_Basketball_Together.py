n, k = map(int,input().split())

x = list(map(int,input().split()))
x.sort()
i = 0
j = n-1

maxi = x[j]
sumi = x[j]
a = 0

while(j>=i):
    if maxi>k:
        a +=1
        j-=1
        maxi = x[j]
        sumi = x[j]
    else:
        maxi += sumi
        i+=1

print(a)
