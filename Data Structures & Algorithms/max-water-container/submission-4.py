class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # T: O(N) | S: O(1)
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            max_area = max(max_area, w * h)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area
