class Solution:
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        length = len(x)
        if length < 4: return False
        x.append(0.1)
        ready = x[2] <= x[0]
        for i in range(3, length):
            if ready and x[i] >= x[i-2]: return True
            if not ready and x[i] <= x[i-2]:
                ready = True
                if x[i] + x[i-4] >= x[i-2]:
                    x[i-1] = x[i-1] - x[i-3]
        return False