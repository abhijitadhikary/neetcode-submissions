class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        idx_l = 0
        idx_r = 1
        profit_max = 0

        while idx_r < len(prices) and idx_l < idx_r:
            if prices[idx_l] > prices[idx_r]:
                idx_l = idx_r
            else:
                profit_c = prices[idx_r] - prices[idx_l]
                profit_max = max(profit_max, profit_c)
            
            idx_r += 1
        return profit_max