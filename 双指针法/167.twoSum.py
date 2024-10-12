def twoSumPairs(nums, target):
    i = 0
    j = len(nums) -1
    pairs = 0
    count = 0
    while i < j:
        temp = target - nums[i]
        print("current number"+ "\t" +str(nums[i]) + "\t" + str(nums[j])  + "\t" + str(temp))
        if i > 0 and nums[i] == nums[i-1]:
            pairs += count
            i += 1
        if nums[i] != nums[i-1]:
            count = 0
            if nums[j] == temp:           
                while nums[j] == temp:
                    count += 1
                    j -= 1
            elif nums[j] < temp:
                i += 1
            else:
                j -= 1
            pairs += count
            print("debug count" + "\t" +str(count))
    return pairs

nums = [-3,-2,-1,-1,-1,0,1,2,2,2,3]
target = 1
res = twoSumPairs(nums, target)
print(res)

