class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        for idx in range(len(prices)-1):
            for idx_2 in range(idx, len(prices)):
                p_c = prices[idx_2] - prices[idx]
                if p_c > max_p:
                    max_p = p_c
        return max_p