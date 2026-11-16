import sys
t= int(input())

for _ in range(t):
    n = int(input())

    a = 0
    b = n
    for i in range(5):
        sys.stdout.flush()
        print(f"? {a+1} {5}")
        f = int(input())
        if f==-1:
            exit()
        
        a += f
        if f==n:
            print("! NO")
            break
        elif f==0:
            print("! NO")
            break
        else:
            if i!=0:
                print("! YES")
                break
            else:
                continue
        