class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # T: O(N) | O(N)
        # N = Size of nums
        counter_nums = Counter(nums)
        max_length = 10**4
        buckets = [[] for _ in range(max_length + 1)]
        result = []
        for num, count in counter_nums.items():
            buckets[count].append(num)
        for i in range(max_length - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
