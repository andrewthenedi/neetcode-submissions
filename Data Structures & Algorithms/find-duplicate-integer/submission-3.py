class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # T: O(N) | S: O(1)
        # N = Size of nums
        dupl = slow = fast = nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        while dupl != slow:
            dupl, slow = nums[dupl], nums[slow]
        return dupl
