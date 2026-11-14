t = int(input())

for _ in range(t):
    n, k  = map(int,input().split())
    x = input()
    l = []
    a = 0
    for i in x:
        if i=="B":
            a +=1
        else:
            l.append(a)