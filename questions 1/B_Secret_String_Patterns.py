import sys
t = int(input())

for _ in range(t):
    n = int(input())
    if n==2:
        sys.stdout.flush()
        print("? 1 1")
        x = int(input())
        if x==1:
            print("! YES")
        elif x==2:
            sys.stdout.flush()
            print("? 2 2")
            y = int(input())
            if y==1:
                print("! YES")
            else:
                print("! NO")
        continue
    for i in range(5):
        sys.stdout.flush()
        print(f"? 1 {n//2}")
        x = int(input())
        

