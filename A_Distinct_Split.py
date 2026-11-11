t = int(input())

for _ in range(t):
    n = int(input())
    x = input()
    sum = 0
    nums1 = set()
    nums2 = {}
    for i in x:
        if i in nums2:
            nums2[i]+=1
        else:
            nums2[i]=1
    
    for i in range(n):
        nums1.add(x[i])
        if nums2[x[i]]==1:
            nums2.pop(x[i])
        else:
            nums2[x[i]] -=1
        
        cur = len(nums1)+len(nums2)
        if sum<cur:
            sum = cur
    print(sum)