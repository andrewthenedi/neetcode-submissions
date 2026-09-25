class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # T: O(N) | S: O(N)
        # N = Size of nums
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False
