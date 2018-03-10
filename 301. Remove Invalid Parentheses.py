class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            cnt = 0
            for c in s:
                cnt += (c == '(') - (c == ')')
                if cnt < 0:
                    return False
            return cnt == 0
        
        level = {s}
        while True:
            valids = list(filter(isValid, level))
            if valids:
                return valids
            level = {s[:i]+s[i+1:] for s in level for i in range(len(s))}