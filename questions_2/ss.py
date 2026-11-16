i = 0
j = 1
nums = [4,2,4,0,0,3,0,5,1,0]
a = 0
while(i<j and j<len(nums)):
    if nums[i]==0 and nums[j]!=0:
        nums[i],nums[j] = nums[j], nums[i]
    elif nums[i]!=0 and nums[j]==0:
        i +=1
        j +=1
    else:
        if nums[i]!=0:
            i +=1
        else:
            j +=1
    a +=1
print(a)
print( nums)