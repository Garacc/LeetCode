class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        i: left idx
        j: right idx
        """
        dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
        for i in reversed(range(len(s))):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][len(s) - 1]

if __name__ == "__main__":
    sol = Solution()
    testcase = "bbcbb"
    print(sol.longestPalindromeSubseq(testcase))