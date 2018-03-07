import math

class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if not c: return True
        
        r = int(math.sqrt(c)) + 1
        for i in range(r):
            tmp = math.sqrt(c - i ** 2)
            if tmp == int(tmp): return True
        return False