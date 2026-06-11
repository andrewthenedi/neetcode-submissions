class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        colder = []
        for i, temp in enumerate(temperatures):
            while colder and colder[-1][0] < temp:
                j = colder[-1][1]
                result[j] = i - j
                colder.pop()
            colder.append([temp, i])
        return result
