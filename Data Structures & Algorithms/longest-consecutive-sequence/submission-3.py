class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # T: O(N) | S: O(N)
        set_nums = set(nums)
        lcs = 0
        for num in set_nums:
            if num - 1 not in set_nums:
                length = 1
                while num + length in set_nums:
                    length += 1
                lcs = max(lcs, length)
        return lcs
