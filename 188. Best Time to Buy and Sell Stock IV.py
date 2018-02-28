class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not k: return 0
        num = len(prices)
        if num < 2: return 0
        if k > num // 2:
            profit = 0
            for i in range(1, num):
                profit += max(0, prices[i] - prices[i - 1])
            return profit

        rel = [0] * k
        buy = [-100000] * k
        for price in prices:
            for i in reversed(range(k)):
                if i > 0:
                    rel[i] = max(rel[i], buy[i] + price)
                    buy[i] = max(buy[i], rel[i - 1] - price)
                else:
                    rel[i] = max(rel[i], buy[i] + price)
                    buy[i] = max(buy[i], - price)
        return rel[k - 1]