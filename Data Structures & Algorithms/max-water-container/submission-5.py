class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # T: O(N) | S: O(1)
        # N = Size of heights
        l, r = 0, len(heights) - 1
        result = 0
        while l < r:
            w, h = r - l, min(heights[l], heights[r])
            result = max(result, w * h)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return result
