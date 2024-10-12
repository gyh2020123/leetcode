def deleteDuplicatesV2(nums):
    n = len(nums)
    if n <=2:
        return n
    j = 2
    for i in range(2, n):
        if nums[i] != nums[j-2]:
            nums[j] = nums[i]
            j +=1
    return j

nums = [0,0,1,1,1,1,1,1,2,3,3]
res = deleteDuplicatesV2(nums)
print(res)
        
        