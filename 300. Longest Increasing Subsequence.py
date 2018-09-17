class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0: return 0
        LIS = [0] * length
        LIS[0] = 1
        for i in range(1, length):
            maxLIS = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    tmpLIS = LIS[j]
                    if tmpLIS > maxLIS:
                        maxLIS = tmpLIS
            LIS[i] = maxLIS + 1
        
        return max(LIS)
            