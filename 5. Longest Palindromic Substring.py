class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return 0
        
        start = 0
        maxlen = 1
        for i in range(len(s)):
            if i - maxlen - 1 >= 0 and s[i-maxlen-1:i+1] == s[i-maxlen-1:i+1][::-1]:
                start = i - maxlen - 1
                maxlen += 2
                continue
            if i - maxlen >= 0 and s[i-maxlen:i+1] == s[i-maxlen:i+1][::-1]:
                start = i - maxlen
                maxlen += 1
                
        return s[start:start + maxlen]