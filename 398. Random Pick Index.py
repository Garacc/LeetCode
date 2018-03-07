import collections
import random

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.numset = collections.defaultdict(set)
        for i in range(len(nums)):
            self.numset[nums[i]].add(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(list(self.numset[target]))
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)