class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        t = [0] * (n+1)
        t[0] = t[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                t[i] += t[j] * t[i-j-1]
        return t[n]