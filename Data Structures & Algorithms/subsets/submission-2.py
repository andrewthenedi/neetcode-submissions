class Solution:
    def iterative(self, nums: List[int]) -> List[List[int]]:
        # T: O(N * 2^n) | S: O(2^N)
        # N = Size of nums
        result = [[]]
        for num in nums:
            result += [subset + [num] for subset in result]
        return result

    def recursive(self, nums: List[int]) -> List[List[int]]:
        # T: O(N * 2^n) | S: O(N + 2^N)
        # N = Size of nums
        result = []
        subset = []
        def dfs(idx: int) -> None:
            if idx == len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[idx])
            dfs(idx + 1)
            subset.pop()
            dfs(idx + 1)
        dfs(0)
        return result

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.iterative(nums)
        # return self.recursive(nums)
        