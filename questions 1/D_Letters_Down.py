t = int(input())

for _ in range(t):
    n = int(input())
    x = input()
    x = list(x)
    i = 0
    j = n-1

    s = 0
    while(i<=j):
        if x[i]!=x[j]:
            s = s + abs(ord(x[i])-ord(x[j]))
            p=max(ord(x[i]),ord(x[j]))
            p1 = min(ord(x[i]),ord(x[j]))
            for v in range(n):
                if ord(x[v])==p:
                    x[v]=chr(p1)
        i +=1   
        j -=1
    print(s)