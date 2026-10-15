class Solution:
    def calculateFinishedHour(self, piles: List[int], k: int) -> int:
        hour = 0
        for pile in piles:
            hour += math.ceil(pile / k)
        return hour

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # T: O(N LOG M) | S: O(1)
        # M = Max of piles
        # N = Size of piles
        l, r = 1, max(piles)
        while l < r:
            mid = l + (r - l) // 2
            if self.calculateFinishedHour(piles, mid) > h:
                l = mid + 1
            else:
                r = mid
        return l
