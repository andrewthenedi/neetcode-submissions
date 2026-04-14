class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # T: O(N) | S: O(N)
        need_to_idx = {}
        for i, num in enumerate(nums):
            if num in need_to_idx:
                return [need_to_idx[num], i]
            need_to_idx[target - num] = i
