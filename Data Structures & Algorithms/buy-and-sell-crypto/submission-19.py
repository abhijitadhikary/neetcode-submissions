class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0
        profit_max = 0
        price_l = prices[0]

        for price_r in prices[1:]:
            if price_r < price_l:
                price_l = price_r
                continue
            profit_max = max(profit_max, price_r - price_l)
            

        return profit_max