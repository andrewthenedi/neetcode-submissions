class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # T: O(N) | S: O(1)
        # N = Size of prices
        max_profit = l = 0
        for r in range(1, len(prices)):
            if prices[l] >= prices[r]:
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
        return max_profit
