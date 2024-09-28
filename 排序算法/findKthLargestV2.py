import random
def findKthLargest(nums, k):
    n = len(nums)
    res = quickSort(nums, k)
    return res

def quickSort(nums, k):
    larger = []
    smaller = []
    equal = []
    n = len(nums)
    pivot = random.randint(0, n-1)
    for num in nums:
        if num > pivot:
            larger.append(num)
        elif num < pivot:
            smaller.append(num)
        else:
            equal.append(num)
    if len(larger) >= k:
        return quickSort(larger, k)
    if len(nums) - len(smaller) < k:
        return quickSort(smaller, k-len(nums)+len(smaller))
    return pivot
    
nums = [3,3,3,3,3,3,3,3,3]
k = 1
res = findKthLargest(nums, k)
print(res)
 