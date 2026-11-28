class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices_prefix_min = []
        min_c = prices[0]
        for price in prices:
            min_c = min(price, min_c)
            prices_prefix_min.append(min_c)
        
        profit_max = -float("inf")
        for idx in range(len(prices)):
            profit_max = max(profit_max, prices[idx] - prices_prefix_min[idx])
        return profit_max