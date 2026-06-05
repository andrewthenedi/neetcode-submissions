class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # T: O(N) | S: O(1)
        # N = Size of numbers
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                break
            if total < target:
                l += 1
            else:
                r -= 1
        return [l + 1, r + 1]
