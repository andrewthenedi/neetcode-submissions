class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # T: O(N) | S: O(N)
        # N = Number of nums
        counter_nums = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counter_nums.items():
            buckets[count].append(num)
        result = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    break
            if len(result) == k:
                break
        return result
