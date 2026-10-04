class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # T: O(N) | S: O(1)
        # N = Size of prices
        max_profit = i = 0
        for j in range(len(prices)):
            if prices[i] < prices[j]:
                max_profit = max(max_profit, prices[j] - prices[i])
            else:
                i = j
        return max_profit
