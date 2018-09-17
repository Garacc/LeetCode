class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        f = s = float('inf')
        for n in nums:
            if n <= f:
                f = n
            elif n <= s:
                s = n
            else:
                return True
        return False