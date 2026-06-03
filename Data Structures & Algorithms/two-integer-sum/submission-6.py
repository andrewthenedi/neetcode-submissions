class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # T: O(N) | S: O(N)
        # N = Number of nums
        num_to_idx = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in num_to_idx:
                return [num_to_idx[need], i]
            num_to_idx[num] = i
        return []
