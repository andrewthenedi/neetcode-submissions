class Solution:
    def get_eating_hours(self, piles: List[int], bananas_per_hour: int):
        eating_hours = 0
        for pile in piles:
            eating_hours += math.ceil(pile / bananas_per_hour)
        return eating_hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l) // 2
            if self.get_eating_hours(piles, m) > h:
                l = m + 1
            else:
                r = m
        return l
