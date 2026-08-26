class Solution:
    def eatingRate(self, piles: List[int], k: int) -> int:
        eating_rate = 0
        for p in piles:
            eating_rate += math.ceil(p / k)
        return eating_rate

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # T: O(N LOG M) | S: O(1)
        # M = Size of piles
        # N = Max of piles
        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l) // 2
            if self.eatingRate(piles, m) > h:
                l = m + 1
            else:
                r = m
        return l
