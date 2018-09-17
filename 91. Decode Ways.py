
class Solution:
    '''
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not len(s):
            return 0
        
        if len(s) == 1:
            if int(s) >=1 and int(s) <= 9:
                return 1
            else:
                return 0
        
        if len(s) == 2:
            if int(s) <= 26:
                if int(s) == 10 or int(s) == 20:
                    return 1
                return 2
            else:
                return 1
            
        dig = int(s[:2])
        if dig == 10 or dig == 20:
            return self.numDecodings(s[2:])
        
        if int(dig) <= 26:
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        
        else:
            return self.numDecodings(s[1:])
    '''
    def numDecodings(self, s):
        v, w, p = 0, int(s>''), ''
        for d in s:
            v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
            return w