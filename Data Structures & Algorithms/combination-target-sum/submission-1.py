class Solution:
    def recursive(self, nums: List[int], target: int) -> List[List[int]]:
        # T: O(N * (T / M)) | S: O(T / M)
        # N = Number of nums
        # T = Number of target
        # M = Min of nums
        nums.sort()
        result = []
        combination = []
        n = len(nums)
        def dfs(start: int, remain: int) -> None:
            if remain == 0:
                result.append(combination.copy())
                return
            for i in range(start, n):
                if nums[i] > remain:
                    continue
                combination.append(nums[i])
                dfs(i, remain - nums[i])
                combination.pop()
        dfs(0, target)
        return result

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.recursive(nums, target)
        