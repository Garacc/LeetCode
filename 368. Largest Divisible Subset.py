from copy import copy

class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        length = len(nums)
        
        if length == 0:
            return []
        subset = [0] * length
        subset[0] = [nums[0]]
        for i in range(1, length):
            maxset = []
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    localset = copy(subset[j])
                    if len(localset) > len(maxset):
                        maxset = localset
            maxset.append(nums[i])
            subset[i] = maxset
        
        ans = []
        for localset in subset:
            if len(localset) > len(ans):
                ans = localset
        
        return ans