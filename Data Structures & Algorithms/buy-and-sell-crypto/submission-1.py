class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # T: O(N) | S: O(1)
        max_profit = l = 0
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
        return max_profit
