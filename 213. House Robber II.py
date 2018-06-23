class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        
        result = [0 for _ in range(len(nums))]
        result[0] = nums[0]
        result[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            result[i] = max(result[i-1], result[i-2] + nums[i])
        
        answer = result[len(nums)-2]
        
        result = [0 for _ in range(len(nums))]
        result[1] = nums[1]
        result[2] = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            result[i] = max(result[i-1], result[i-2] + nums[i])
        
        answer = max(answer, result[len(nums)-1])
        
        return answer