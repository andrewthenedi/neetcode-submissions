class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # T: O(N) | S: O(N)
        # N = Size of temperatures
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                pos = stack.pop()
                result[pos] = i - pos
            stack.append(i)
        return result
