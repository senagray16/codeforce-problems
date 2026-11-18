from collections import deque
x = input()

y = deque()

for i in x:
    if len(y)==0:
        y.append(i)
    elif y[-1]!=i:
        y.append(i)
    else:
        y.pop()
if len(y)==0:
    print("Yes")
else:
    print("No")