class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # T: O(N) | S: O(1) excluding output
        # N = Number of nums
        result = [1] * len(nums)
        prefix = suffix = 1

        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]
        
        for i in range(len(nums) -1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
