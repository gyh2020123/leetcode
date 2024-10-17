def findMaxLength(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        zeroCnt = 0
        oneCnt = 0
        l, r = 0, 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                zeroCnt += 1
            if nums[i] == 1:
                oneCnt += 1
        print("%s %s" % (zeroCnt, oneCnt))
        while r < n:
            if nums[r] == 0:
                zeroCnt += 1
            if nums[r] == 1:
                oneCnt += 1
            if zeroCnt == oneCnt:
                res = max(res, zeroCnt*2)
            r += 1
        print(res)
        while l < n:
            if nums[l] == 0:
                zeroCnt -= 1
            if nums[l] == 1:
                oneCnt -= 1
            if zeroCnt == oneCnt:
                res = max(res, zeroCnt*2)
            l += 1
        print(res)
        return res

nums = [0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]
print(len(nums))
print(findMaxLength(nums))