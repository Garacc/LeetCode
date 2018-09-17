class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ori = list(str(x))
        rev = list(reversed(str(x)))
        for i in range(len(ori)):
            if ori[i] != rev[i]:
                return False
        
        return True