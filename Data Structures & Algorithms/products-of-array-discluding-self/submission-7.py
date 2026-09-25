class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # T: O(N) | S: O(1)
        # N = Size of nums
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums) - 1):
            prefix *= nums[i]
            result[i + 1] = prefix
        suffix = 1
        for i in range(len(nums) - 1, 0, -1):
            suffix *= nums[i]
            result[i - 1] *= suffix
        return result
