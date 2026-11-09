x = input()
x = list(x)

if "h" not in x:
    print("NO")
elif "e" not in x:
    print("NO")
elif x.count("l")<2:
    print("NO")
elif "o" not in x:
    print("NO")
else:
    li = []
    for i in x:
        if len(li)==0:
            if i=="h":
                li.append(i)
        if len(li)==1:
            if i=="e":
                li.append(i)
        if len(li)==2 or len(li)==3:
            if i=="l":
                li.append(i)
        if len(li)==4:
            if i=="o":
                li.append(i)
    a = "".join(li)
    if a=="hello":
        print("YES")
    else:
        print("NO")

