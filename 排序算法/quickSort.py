def quickSort(nums, l, r):
    pivot = nums[l]
    i, j = l+1, r
    # while(i <= j):
    #     print(str(i) + "\t" + str(j))
    #     while nums[i] < pivot:
    #         i+=1  
    #     while nums[j] > pivot:
    #         j-=1
    #     # i指向大于pivot的元素，j指向小于pivot的元素，交换i，j位置的元素
    #     if i < j:
    #         nums[i], nums[j] = nums[j], nums[i]
    #     i += 1
    #     j -= 1
    while i <= j and nums[j] >= pivot:
        j -= 1
        nums[i] = nums[j]
    while i <= j and nums[i] <= pivot:
        i += 1
        nums[j] = nums[i]

    nums[l] = pivot
    quickSort(nums, l, i-1)
    quickSort(nums, j+1, r)
    return nums

# nums = [3,3,3,3,3,3,3,3,3]
nums = [3,4,7,2,6,5]
nums = quickSort(nums, 0, len(nums)-1)
print(nums)