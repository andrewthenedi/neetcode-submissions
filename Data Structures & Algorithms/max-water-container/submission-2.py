class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # T: O(N) | S: O(1)
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            width = r - l
            if heights[l] < heights[r]:
                height = heights[l]
                l += 1
            else:
                height = heights[r]
                r -= 1
            area = width * height
            max_area = max(max_area, area)
        return max_area
