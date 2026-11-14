t = int(input())

for _ in range(t):
    n = int(input())
    li = []
    for _ in range(n):
        y = list(map(int, input().split()))
        x = y[1:]
        a = max(x[j] - j + 1 for j in range(len(x)))
        b = a + len(x)
        li.append((a, b))

    li.sort()

    ans = 0
    gain = 0
    for a, b in li:
        if a - gain > ans:
            ans = a - gain
        gain += b - a

    print(ans)