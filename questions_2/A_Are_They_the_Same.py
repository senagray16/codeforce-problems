t = int(input())

for _ in range(t):
    n,k = map(int,input().split())

    x = list(map(int,input().split()))
    y = list(map(int,input().split()))

    a = 0
    b=0
    for i in range(n):
        if x[i]%2==0:
            a+=1
        if y[i]%2==0:
            b +=1


    if a==b:
        print("YES")
        continue
    elif a>b:
        if k%2==1:
            print("YES")
        else:
            print("NO")
    else:
        if k%2==0:
            print("YES")
        else:
            print("NO")
