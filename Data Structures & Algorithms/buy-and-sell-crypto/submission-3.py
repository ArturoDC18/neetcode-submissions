class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minf = 1000
        profit = 0 
        for price in prices:
            minf = min(minf,price)
            profit = max(profit, price-minf)
        return profit