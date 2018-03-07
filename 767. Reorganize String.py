class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        newS = sorted(sorted(S), key = S.count)
        length = len(S) // 2
        newS[1::2], newS[::2] = newS[:length], newS[length:]
        return ''.join(newS) * (newS[-1:] != newS[-2:-1])
        