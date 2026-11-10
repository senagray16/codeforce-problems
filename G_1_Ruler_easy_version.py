import sys
t = int(input())

for _ in range(t):
    i,j = 2,999
    for v in range(10):
        sys.stdout.flush()
        mid = (i+j)//2
        print(f"? {mid} {1}")
        a = int(input())
        if a==1*mid:
            i = mid + 1
        else:
            ans = mid
            j = mid-1
            
    print(f"! {ans}")
        