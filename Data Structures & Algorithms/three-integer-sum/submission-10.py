class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # T: O(N^2) | S: O(1)
        # N = Size of nums
        result = []
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum < 0:
                    j += 1
                elif curr_sum > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while j < k and nums[j] == nums[k + 1]:
                        k -= 1
        return result
