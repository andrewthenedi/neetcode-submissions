class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # T: O(N LOG K) | S: O(K)
        self.min_heap = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # T: O(LOG K) | S: O(1)
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        return self.min_heap[0]
