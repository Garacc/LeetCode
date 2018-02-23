class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''
        
        for i in reversed(range(len(s))):
            if s[0:i] == s[0:i][::-1]:
                break
        return s[i:len(s)][::-1] + s