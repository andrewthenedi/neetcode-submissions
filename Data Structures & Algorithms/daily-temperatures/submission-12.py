class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # T: O(N) | S: O(N)
        # N = Size of temperatures
        result = [0] * len(temperatures)
        colder_idx = []
        for i, temp in enumerate(temperatures):
            while colder_idx and temperatures[colder_idx[-1]] < temp:
                j = colder_idx.pop()
                result[j] = i - j
            colder_idx.append(i)
        return result
