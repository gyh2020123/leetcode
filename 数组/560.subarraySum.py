def subarraySum(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, 0
        n = len(nums)
        sumk = 0
        count = 0
        while l <= n and r <= n:
            print("%s %s" %(l, r))
            if sumk == k:
                count += 1
                r += 1
            elif sumk < k:
                sumk += nums[r]
                r += 1
            else:
                sumk -= nums[l]
                l += 1
        return count

nums = [1,1,1]
k = 2
res = subarraySum(nums, k)
print(res)