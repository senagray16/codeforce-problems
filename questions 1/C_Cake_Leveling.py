t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))

    swiped = 0
    last = x[0]
    f = [last]

    for i in range(1, n):
        if x[i] < last:
            swiped += last - x[i]
            last = x[i]
        else:
            last = x[i]
        f.append(last)

    print(swiped)
    print(f)