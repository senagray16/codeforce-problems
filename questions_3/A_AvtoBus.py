t = int(input())
for _ in range(t):
    n = int(input())
    c = 0
    if n%2==1 or n==2:
        c = -1
    
    if n%4 == 0:
        a = n // 4
    elif n%4 == 2:
        a = n // 4 

    if n<6:
        b = a
    elif n%6 == 0:
        b = n//6
    elif n%6==2:
        b = n//6 + 1
    elif n%6==4:
        b = n//6 + 1

    
    if c==-1:
        print(-1)
    else:
        print(b,a)