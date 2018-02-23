import collections

class Solution:
    '''
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if set(s) & set(t) != set(t): return ''
        
        minwin = s
        ele = set(t)
        start = 0
        for end in range(len(s)):
            tmp = s[start:end]
            tmpset = set(tmp) 
            while tmpset & ele == ele:
                if len(tmp) < len(minwin):
                    minwin = tmp
                start += 1
                tmp = s[start:end]
                tmpset = set(tmp)
        return minwin
    '''
    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]

if __name__ == '__main__':
    s = 'ADOBECODEBANC'
    t = 'ABC'
    sol = Solution()
    print(sol.minWindow(s, t))