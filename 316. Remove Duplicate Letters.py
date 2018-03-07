class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(suffix) == set(s):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''
    '''
    def removeDuplicateLetters(self, s):
        result = ''
        while s:
            idx = min(map(s.rindex, set(s)))
            c = min(s[:idx+1])
            result += c
            s = s[s.index(c):].replace(c, '')
        return result
    '''