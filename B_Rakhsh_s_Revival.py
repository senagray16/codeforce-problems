t = int(input())

for _ in range(t):
    n, m, k = list(map(int,input().split()))
    x = input()

    a = 0
    posion = k
    num = 0
    for i in x:
        if i=="1" and posion==k:
            a = 0
            continue
        else:
            if a!=m-1:
                a = a + 1
            else:
                if posion==k:
                    num +=1
                posion -=1
                if posion==0:
                    a = 0
                    posion = k
                
                
    print(num)
