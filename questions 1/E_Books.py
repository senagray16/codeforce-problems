n,m = map(int,input().split())

x = list(map(int,input().split()))

i = 1
j = 1
xnew = [0]
sum = 0
for v in x:
    sum+=v
    xnew.append(v)
xnew.append(0)
num = 0
maxnum = 0

while(j<n):

    s = xnew[j]-xnew[i-1]

    if s > m:
        if num==0:
            num = 0
        else:
            num = num - 1
        i = i + 1
    else:
        num = num + 1
        j = j + 1
    if num> maxnum:
        maxnum = num
print(maxnum)
