t = int(input())

for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))

    for i in range(n):
        if i == 0:
            high = x[0]   
            low = x[0]    
            ans = x[0]    
        else:
            
            best = max(x[i] - high, x[i], x[i] + high, x[i] - low, x[i] + low)
            if best > ans:
                ans = best

            
            high1 = max(x[i], high + x[i], 2 * high + x[i], low + x[i], 2 * low + x[i])
            low1 = min(x[i], high + x[i], 2 * high + x[i], low + x[i], 2 * low + x[i])

            high = high1
            low = low1

    print(ans)