class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # T: O(N) | S: O(N)
        # N = Size of nums
        set_nums = set()
        for num in nums:
            if num in set_nums:
                return True
            set_nums.add(num)
        return False
