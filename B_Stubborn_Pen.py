t = int(input())

for _ in range(t):
    n = int(input())
    last = "R"
    a = 0
    x = input()
    for i in x:
        if i!=last:
            a +=1
            if i=="R":
                last = "B"
            else:
                last = "R"
        else:
            if i=="R":
                last = "B"
            else:
                last = "R"
    print(a)