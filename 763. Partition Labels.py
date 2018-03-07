class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        output = []
        while S:
            for i in range(len(S)):
                maxidx = 0
                for c in S[:i+1]:
                    maxidx = max(maxidx, S.rindex(c))
                if maxidx == i:
                    output.append(maxidx+1)
                    S = S[i+1:]
                    break
        return output
    '''
    def partitionLabels(self, S):
        sizes = []
        while S:
            i = 1
            while set(S[:i]) & set(S[i:]):
                i += 1
            sizes.append(i)
            S = S[i:]
        return sizes
    '''