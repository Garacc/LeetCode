class Solution:
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        num = len(stickers)
        mp = [[0] * 26 for _ in range(num)]
        for i in range(num):
            for word in stickers[i]:
                mp[i][ord(word) - ord('a')] += 1
        dp = {}
        dp[''] = 0
        
        def match(dp, mp, target):
            if target in dp:
                return dp[target]
            n = len(mp)
            tar = [0] * 26
            for word in target:
                tar[ord(word) - ord('a')] += 1
            ans = 10000
            for i in range(n):
                if mp[i][ord(target[0]) - ord('a')] == 0: continue
                s = ''
                for j in range(26):
                    if tar[j] > mp[i][j]:
                        s += chr((ord('a') + j)) * (tar[j] - mp[i][j])
                tmp = match(dp, mp, s)
                if tmp != -1:
                    ans = min(ans, tmp + 1)
            dp[target] = -1 if ans == 10000 else ans
            return dp[target]
        
        return match(dp, mp, target)
                
            