class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n < 2:
            return 0
        
        profit_max = 0
        
        idx_r = 1
        idx_l = 0

        while idx_r < n:
            price_l = prices[idx_l]
            price_r = prices[idx_r]
            if price_r <= price_l:
                idx_l = idx_r
            else:
                profit_max = max(profit_max, price_r - price_l)
            idx_r += 1
        return profit_max