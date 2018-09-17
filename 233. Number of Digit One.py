class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        
        pre, x, ans = n, 1, 0
        while pre > 0:
            dig = pre % 10
            pre //= 10
            ans += pre * x
            if dig == 1:
                ans += n % x + 1
            elif dig > 1:
                ans += x
            x *= 10
            
        return ans