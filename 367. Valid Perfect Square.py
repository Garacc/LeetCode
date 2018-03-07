class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num == (self.mySqrt(num) ** 2)
        
    '''
    copy from 69
    '''
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r