def findKthLargest(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n= len(nums)
        return quickSelect(nums, 0, n-1, n-k)

def quickSelect(nums, l, r, k):
    if l == r: return nums[k]
    pivot = nums[l]
    i, j = l+1, r
    if i == j:
        if nums[i] < pivot:
            nums[i], nums[l] = nums[l], nums[i]
    while i < j:
        while i <= r and nums[i] < pivot: i+=1 #处理边界情况
        while j >= l and nums[j] > pivot: j-=1 #处理边界情况
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    # i,j碰撞的时候，将pivot换到j的位置，保持数组有序
    if i != j and j != l:
        nums[l], nums[j] = nums[j], nums[l]
    
    if k == j:
        return nums[k]
    elif k < j:
        return quickSelect(nums, l, j-1, k)
    else:
        return quickSelect(nums, j+1, r, k)
    

nums = [3,3,3,3,3,3,3,3,3]
k = 1
res = findKthLargest(nums, k)
print(res)
