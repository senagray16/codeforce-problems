t = int(input())

for _ in range(t):
    n = int(input())

    x = list(map(int,input().split()))

    even = []
    odd = []
    for i in x:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    a = 0
    if len(even)%2==0 or len(odd)%2==0:
        a = 1
        print("YES")
    else:
        for i in even:
            if (i+1 in odd) or (i-1 in odd):
                a = 1
                print("YES")
                break
    
    if a==0:
        print("NO")


