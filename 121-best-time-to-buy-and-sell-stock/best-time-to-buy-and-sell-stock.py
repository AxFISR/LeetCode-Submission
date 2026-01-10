class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        maxSell = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            if(prices[buy] < prices[sell]):
                profit = prices[sell] - prices[buy]
                maxSell = max(profit,maxSell)
            else:
                buy = sell
            sell+=1
        return maxSell