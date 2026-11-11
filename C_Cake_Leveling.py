t = int(input())

for _ in range(t):
    n=int(input())
    x = list(map(int,input().split()))
    result = []
    sum = x[0]
    num = 0
    for i in x[1:]:
        if i<sum:
            result.append(i)
            sum = i
            rest = sum * num - num*i
        elif i==sum:
            result.append(i)
        else:



