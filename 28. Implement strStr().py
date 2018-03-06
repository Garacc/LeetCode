class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack: return -1
        if not needle: return 0
        
        return haystack.index(needle)