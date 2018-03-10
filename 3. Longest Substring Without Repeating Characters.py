class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        maxlen = 0
        #start, end = 0, 0
        visited = set()
        for i in range(len(s)):
            if s[i] not in visited:
                visited.add(s[i])
                if i - left + 1 > maxlen:
                    maxlen = i - left + 1
                    #start = left
                    #end = i + 1
            else:
                left += s[left:i].index(s[i]) + 1
                visited = set(s[left:i+1])
        #return s[start:end]
        return maxlen
        
if __name__ == "__main__":
    sol = Solution()
    testcase = "bbtablud"
    print(sol.lengthOfLongestSubstring(testcase))