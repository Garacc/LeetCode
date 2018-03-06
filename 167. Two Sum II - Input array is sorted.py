class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1
        while l < r:
            ans = nums[l] + nums[r]
            if ans == target:
                return [l+1, r+1]
            elif ans < target:
                l += 1
            else:
                r -= 1