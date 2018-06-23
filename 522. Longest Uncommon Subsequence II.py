class Solution:
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def subSeq(word1, word2):
            #check if word1 is a subseq of word2
            i = 0
            for char in word2:
                if i < len(word1) and word1[i] == char:
                    i += 1
            return i == len(word1)
        
        strs.sort(key = len, reverse = True)
        for i, word1 in enumerate(strs):
            if all(not subSeq(word1, word2) for j, word2 in enumerate(strs) if j != i):
                return len(word1)
        
        return -1