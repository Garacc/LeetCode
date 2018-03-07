class Solution:
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        num = 0
        for w in b:
            num *= 10
            num += w
        return pow(a, num, 1337)