n, k = map(int, input().split())

x = list(map(int, input().split()))
x.sort()

a = n // 2
ans = x[a]
count = 1  

for i in range(a + 1, n):
    diff = x[i] - ans
    cost = diff * count
    if k >= cost:
        k -= cost
        ans = x[i]
        count += 1
    else:
        ans += k // count
        k = 0
        break

if k > 0:
    ans += k // count

print(ans)