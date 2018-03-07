class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str: return 0
        
        num = 0
        flag = 1
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        while str[0] == ' ':
            str = str[1:]
            if not str: return 0
            
        if str[0] == '-':
            flag = -1
        if str[0] == '-' or str[0] == '+':
            str = str[1:]
        for c in str:
            if '0' <= c <= '9':
                num *= 10
                num += int(c)
            else:
                break
        num = flag * num
        if num >= 0:
            return num if num < INT_MAX else INT_MAX
        else:
            return num if num > INT_MIN else INT_MIN