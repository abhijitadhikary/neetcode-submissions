class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n < 2:
            return 0
        
        profit_max = 0
        price_min = prices[0]

        for idx in range(1, n):
            price_c = prices[idx]
            profit_max = max(profit_max, price_c - price_min)
            price_min = min(price_min, price_c)
        return profit_max