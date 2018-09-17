class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while(n > 1):
            count += n // 5
            n //= 5
        return count