class Solution:
    def recursive(self, nums: List[int]) -> List[List[int]]:
        # T: O(N * 2 ^ N) | S: O(N)
        # N = Number of nums
        result, sub_result = [], []
        n = len(nums)
        def dfs(start: int) -> None:
            if start == n:
                result.append(sub_result.copy())
                return
            sub_result.append(nums[start])
            dfs(start + 1)
            sub_result.pop()
            dfs(start + 1)
        dfs(0)
        return result

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.recursive(nums)
        