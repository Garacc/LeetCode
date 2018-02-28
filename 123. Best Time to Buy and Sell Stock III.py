class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        rel1, rel2 = 0, 0
        buy1, buy2 = -100000, -100000
        for price in prices:
            rel2 = max(rel2, buy2 + price)
            buy2 = max(buy2, rel1 - price)
            rel1 = max(rel1, buy1 + price)
            buy1 = max(buy1, - price)
        return rel2