t = int(input())

for _ in range(t):
    n = int(input())

    x = list(map(int,input().split()))
    a = max(x)
    ans = -1
    for i in range(n):
        if x[i]==a:
            if i==0:
                if x[i+1]!=a:
                    ans = i
                    break
            elif i==n-1:
                if x[i-1]!=a:
                    ans = i
                    break
            else:
                if x[i-1]!=a or x[i+1]!=a:
                    ans = i
                    break
    if ans==-1:
        print(ans)
    else:
        print(ans+1)
