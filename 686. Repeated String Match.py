class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        s = A
        while len(s) < 2 * len(A) + len(B):
            if B in s: return len(s) // len(A)
            s += A
        return -1