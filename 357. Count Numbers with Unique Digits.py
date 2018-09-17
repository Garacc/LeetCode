class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        else:
            m = n - 1
            ans = 9
            tmp = 9
            while m:
                ans = ans * tmp
                tmp -= 1
                m -= 1
            return ans + self.countNumbersWithUniqueDigits(n-1)