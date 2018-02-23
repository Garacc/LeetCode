class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        count = 0
        for i in range(len(s)):
            for j in range(len(s) - i):
                if s[i:i+j+1] == s[i:i+j+1][::-1]:
                    count += 1
        return count
                

