class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        maxjump = 0
        for pos, jump in enumerate(nums):
            if pos > maxjump:
                return False
            maxjump = max(maxjump, pos+jump)
            if maxjump >= length:
                return True
        return True
        