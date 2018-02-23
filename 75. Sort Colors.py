class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        for k in range(len(nums)):
            value = nums[k]
            nums[k] = 2
            if value < 2:
                nums[j] = 1
                j += 1
            if value == 0:
                nums[i] = 0
                i += 1