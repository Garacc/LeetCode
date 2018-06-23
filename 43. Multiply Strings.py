class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        n1, n2 = 0, 0
        
        for i in range(len(num1)):
            n1 = n1 * 10 + int(num1[i])
        
        for i in range(len(num2)):
            n2 = n2 * 10 + int(num2[i])
        
        ans = n1 * n2
        return str(ans)