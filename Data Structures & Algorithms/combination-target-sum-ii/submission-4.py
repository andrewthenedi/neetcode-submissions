class Solution:
    def recursive(self, candidates: List[int], target: int) -> List[List[int]]:
        # Time: O(N ^ (T / M)) | S: O(T / M)
        # N = Number of candidates
        # T = Number of target
        # M = Min of candidates
        candidates.sort()
        result, sub_result = [], []
        n = len(candidates)
        def dfs(start: int, remain: int) -> None:
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remain:
                    break
                sub_result.append(candidates[i])
                if candidates[i] == remain:
                    result.append(sub_result.copy())
                else:
                    dfs(i + 1, remain - candidates[i])
                sub_result.pop()
        dfs(0, target)
        return result

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.recursive(candidates, target)
        