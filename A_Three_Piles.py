t = int(input())

for _ in range(t):
    a,b,c = list(map(int,input().split()))
    x = sorted([a,b,c])
    if x[0]+1==x[1] and x[1]+1==x[2]:
        print("YES")
    else:
        print("NO")
    