class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0
        profit_max = 0
        price_l = prices[0]
        for index in range(1, len(prices)):
            price_r = prices[index]
            profit_max = max(profit_max, price_r - price_l)
            price_l = min(price_r, price_l)

        return profit_max