n,k = map(int,input().split())

x = list(map(int,input().split()))
x.sort()

y = [0]*(n+1)
for i in range(k):
    a,b = map(int,input().split())
    y[a-1]+=1
    y[b]-=1
curr = 0
for i in range(n+1):
    curr = curr + y[i]
    y[i]=curr
y = y[:n]
y.sort()
h = 0
for i in range(n):
    h += (y[i]*x[i])
print(h)