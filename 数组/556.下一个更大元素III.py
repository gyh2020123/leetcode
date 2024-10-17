def nextGreaterElement(n):
        """
        :type n: int
        :rtype: int
        """
        nums = list(str(n))
        m = len(nums)
        i = m -2
        # 从后往前找第一个升序的index
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i < 0:
            return -1
        # 从后往前找第一个大于升序index数值的数，与升序index数值进行交换，保证增加的数值最小
        j = len(nums) -1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        # i之后的降序数值进行翻转，成为升序，最小数值
        # k = len(nums) -1
        # while i+1 < k:
        #     nums[i+1], nums[k] = nums[k], nums[i+1]
        #     i+=1
        #     k-=1
        nums[i+1:] = nums[i+1:][::-1]
        res = int(''.join(nums))
        return res if res < 2**31 else -1
n = 101
print(nextGreaterElement(n))