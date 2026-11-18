n = int(input())
x = list(map(int,input().split()))

xsum = 0
x1 = []
for i in x:
    xsum +=i
    x1.append(xsum)

q = int(input())
y = list(map(int,input().split()))


for i in y:
    ind = -1
    a = 0
    b = len(x1)-1
    while(b>=a):
        mid = (a+b)//2
        if x1[mid]>=i:
            ind = mid
            b = mid-1
        else:
            a = mid+1
    if ind==-1:
        ind = len(x)-1
    print(ind+1)

