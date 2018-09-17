class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def gcd(x, y):
            while(y > 0):
                r = x % y
                x = y
                y = r
            return x
        t = p * q / (gcd(p, q))
        if (t // q) % 2 == 0:
            return 2
        elif (t // p) % 2 == 0:
            return 0
        else:
            return 1