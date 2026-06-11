class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # T: O(N) | S: O(N)
        result = [0] * len(temperatures)
        colder = []
        for i, temp in enumerate(temperatures):
            while colder and temperatures[colder[-1]] < temp:
                j = colder.pop()
                result[j] = i - j
            colder.append(i)
        return result
