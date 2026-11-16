t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    pairs = []
    for i in range(n):
        pairs.append((y[i], x[i]))
    pairs.sort()
    cost = k
    people = 1
    for i, j in pairs:
        if people == n:
            break
        elif i >= k:
            cost += k * (n - people)
            people = n
        else:
            if j <= n - people:
                people += j
                cost += i * j
            else:
                cost += (n - people) * i
                people = n

    print(cost)