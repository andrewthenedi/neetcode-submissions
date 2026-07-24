class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # T: O(N) | S: O(N)
        # N = Size of nums
        max_nums_length = 10^4
        top_k_frequent = []
        buckets = [[] for _ in range(max_nums_length)]
        counter_nums = Counter(nums)
        for num, count in counter_nums.items():
            buckets[count].append(num)
        for i in range(max_nums_length - 1, -1, -1):
            if not buckets[i]:
                continue
            for num in buckets[i]:
                top_k_frequent.append(num)
                if len(top_k_frequent) == k:
                    return top_k_frequent
