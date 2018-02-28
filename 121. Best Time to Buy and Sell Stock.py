class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        curpro = 0
        for i in range(1, len(prices)):
            curpro += prices[i] - prices[i - 1]
            curpro = max(0, curpro)
            profit = max(curpro, profit)
        return profit
    '''
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices) - 1):
            profit = max(profit, max(prices[i+1:]) - prices[i])
        return profit
        TLE
    '''