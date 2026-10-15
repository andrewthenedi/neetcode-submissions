class Solution:
    def findMin(self, nums: List[int]) -> int:
        # T: O(LOG N) | S: O(1)
        # N = Size of nums
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
