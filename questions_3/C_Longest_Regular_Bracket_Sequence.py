from collections import deque
x = input()
y = deque()
dik = {}
a = 0
for i in x:
    if i == "(":
        y.append(i)
        a += 1
    else:
        if len(y)==0:
            if a!=0:
                if a in dik:
                    dik[a] +=1
                else:
                    dik[a] = 1
            a = 0
        else:
            a += 1
            y.pop()
if a!=len(y):
    a = a - len(y)
    if a in dik:
        dik[a] +=1
    else:
        dik[a] = 1

if dik=={}:
    print(0,1)
else:
    a = max(dik)
    print(a,dik[a])

