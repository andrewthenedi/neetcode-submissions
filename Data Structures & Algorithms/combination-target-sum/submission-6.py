class Solution:
    def recursive(self, nums: List[int], target: int) -> List[List[int]]:
        # Time: O(N ^ (T / M)) | S: O(T / M)
        # N = Number of nums
        # T = Number of target
        # M = Min of nums
        nums.sort()
        result, sub_result = [], []
        n = len(nums)
        def dfs(start: int, remain: int):
            for i in range(start, n):
                if nums[i] > remain:
                    break
                sub_result.append(nums[i])
                if nums[i] == remain:
                    result.append(sub_result.copy())
                else:
                    dfs(i, remain - nums[i])
                sub_result.pop()
        dfs(0, target)
        return result

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.recursive(nums, target)
        