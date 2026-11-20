t = int(input())

for _ in range(t):
    n,x,y = list(map(int,input().split()))
    inp = list(map(int,input().split()))

    before = inp[:x]
    middle = inp[x:y]
    after = inp[y:]
    main = before + after

    min1 = middle.index(min(middle))
    middle = middle[min1:]+middle[:min1]

    ans = len(main)
    for i in range(len(main)):
        if main[i]>middle[0]:
            ans = i
            break

    result = main[:ans] + middle + main[ans:]
    for i in result:
        print(i, end=" ")
    print(end="\n")
        
