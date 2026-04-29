class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxProfit = 0
        for i in range(1,len(prices)):
            if prices[i] - mini > maxProfit:
                maxProfit = prices[i] - mini
            if prices[i] < mini:
                mini = prices[i]
        return maxProfit
        