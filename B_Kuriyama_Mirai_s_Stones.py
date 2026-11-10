t = int(input())

x = list(map(int,input().split()))
sum = 0
xsum = []
for i in x:
    sum +=i
    xsum.append(sum)


xsorted = sorted(x)
sum = 0
xsortedsum = []
for i in xsorted:
    sum +=i
    xsortedsum.append(sum)

n=int(input())
for i in range(n):
    n,l,k = list(map(int,input().split()))
    if n==1:
        print(xsum[k-1] - xsum[l-1] + x[l-1])
    else:
        print(xsortedsum[k-1] - xsortedsum[l-1]+xsorted[l-1])
    