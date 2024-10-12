def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    def reverse(nums, firstIndex, lastIndex):
        i, j = firstIndex, lastIndex
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        print(nums)
    # 找到第一个升序的index
    n = len(nums)
    i, j, k = n-2, n-1, n-1
    while i >= 0 and nums[i] >= nums[j]:
        i -= 1
        j -= 1
    if i == -1:
        reverse(nums)
        return
    # 从后往前找第一个大于升序index的值
    while i >= 0 and nums[i] > nums[k]:
        k -= 1
    # 交换
    nums[i], nums[k] = nums[k], nums[i]
    # 翻转i以后的降序数组
    print("before %s i %s" % (nums,i))
    reverse(nums, i+1, n-1)
    print("after %s" %nums)


def reverse(nums):
    i, j = 0, len(nums)-1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums
    
nums = [1, 3, 2]
nextPermutation(nums)
# print(nums[1:])
# print(reverse(nums[1:]))
print(nums)
