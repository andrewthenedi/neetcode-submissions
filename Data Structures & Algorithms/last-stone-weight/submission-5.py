class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # T: O(N LOG N) | S: O(N)
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            x, y = heapq.heappop(max_heap), heapq.heappop(max_heap)
            remain = x - y
            if remain:
                heapq.heappush(max_heap, remain)
        return -max_heap[0] if max_heap else 0
