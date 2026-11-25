class Solution:
    def recursive(self, candidates: List[int], target: int) -> List[List[int]]:
        # T: O(N * 2 ^ N) | S: O(N)
        # N = Number of candidates
        result, sub_result = [], []
        n = len(candidates)
        candidates.sort()
        def dfs(start: int, remain: int):
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
        