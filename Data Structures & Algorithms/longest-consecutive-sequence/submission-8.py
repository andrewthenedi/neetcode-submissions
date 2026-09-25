class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # T: O(N) | S: O(N)
        # N = Size of nums
        set_nums = set(nums)
        lcs = 0
        for num in nums:
            if num - 1 not in set_nums:
                length = 0
                while num in set_nums:
                    length += 1
                    num += 1
                lcs = max(lcs, length)
        return lcs
