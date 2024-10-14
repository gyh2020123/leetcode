def twoSumPairs(nums, target):
    i = 0
    j = len(nums) -1
    pairs = 0
    count = 0
    while i < j:
        temp = target - nums[i]
        print("current number"+ "\t" + str(i) + "\t" + str(j)  + "\t" + str(temp))  
        if i > 0 and nums[i] == nums[i-1]:
            pairs += count
            i += 1
            print("copy debug count" + "\t" +str(count))
        else:
            if nums[j] == temp:  
                count = 0  #注意是在遇到有和temp相同的值的时候才将count置为0，否则i和j指针只要移动，则会发生置0的情况
                while nums[j] == temp:
                    count += 1
                    j -= 1
                pairs += count #注意是在遍历完指向相同元素的j之后就要增加pairs的数量，否则由于j指针变动，pairs会多加数值
            elif nums[j] < temp:
                i += 1
            else:
                j -= 1
            print("debug count" + "\t" +str(count))
    return pairs

nums = [-3,-2,-1,-1,-1,0,1,2,2,2,3]
target = 1
res = twoSumPairs(nums, target)
print(res)

# count = 0
# print("Before modification:", count)

# count += 1
# print("After modification:", count)

