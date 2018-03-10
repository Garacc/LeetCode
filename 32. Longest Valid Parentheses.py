class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = ')' + s
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')' and s[i-dp[i-1]-1] == '(':
                dp[i] = 2 + dp[i-1] + dp[i-dp[i-1]-2]
        return max(dp)
    
if __name__ == "__main__":
    testcase = "())()(()"
    sol = Solution()
    print(sol.longestValidParentheses(testcase))