class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n < 2:
            return 0
        
        profit_max = 0
        
        idx_r = 1
        idx_l = 0

        while idx_r < n:
            if prices[idx_r] <= prices[idx_l]:
                idx_l = idx_r
            else:
                profit_max = max(profit_max, prices[idx_r] - prices[idx_l])
            
            idx_r += 1
        return profit_max