class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # T: O(N) | S: O(1)
        # N = Size of nums
        n = len(nums)
        product_except_self = [1] * n
        prefix = 1
        for i in range(n - 1):
            prefix *= nums[i]
            product_except_self[i + 1] = prefix
        suffix = 1
        for i in range(n - 1, 0, -1):
            suffix *= nums[i]
            product_except_self[i - 1] *= suffix
        return product_except_self
