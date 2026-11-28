class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max = -float("inf")
        price_min = float("inf")

        for price in prices:
            price_min = min(price_min, price)
            profit_max = max(profit_max, price - price_min)
        return profit_max