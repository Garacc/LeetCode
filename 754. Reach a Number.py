import math

class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target < 0:
            target = -1 * target
        if target == 0:
            return 0
        
        n = math.floor(math.sqrt(2 * target))
        
        while(1):
            to_minus = n * (n + 1) // 2 - target
            if to_minus >= 0:
                if to_minus % 2 == 0:
                    return int(n)
            n += 1