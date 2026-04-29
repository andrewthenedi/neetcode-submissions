class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # T: O(N) | S: O(1)
        first, second = cost[0], cost[1]
        for i in range(2, len(cost)):
            first, second = second, cost[i] + min(first, second)
        return min(first, second)
