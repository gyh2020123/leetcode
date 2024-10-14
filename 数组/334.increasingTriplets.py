def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    if n < 3:
        return False
    leftMin = [0] * n
    leftMin[0] = nums[0]
    rightMax = [0] * n
    rightMax[-1] = nums[-1]
    for i in range(1, n):
        leftMin[i] = min(leftMin[i-1], nums[i-1])
    for j in range(n-2, 0, -1):
        rightMax[j] = max(rightMax[j+1], nums[j+1])
    for k in range(1, n):
        if nums[k] > leftMin[k] and nums[k] < rightMax[k]:
            return True
    return False

nums = [1,5,0,4,1,3]
print(increasingTriplet(nums))