class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # T: O(M * N) | S: O(M * N)
        # M = Size of grid rows
        # N = Size of grid columns
        visited = set()
        queue = collections.deque()
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]
        m, n = len(grid), len(grid[0])
        minute = n_fresh = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    n_fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
        while queue:
            for _ in range(len(queue)):
                r_rotten, c_rotten = queue.popleft()
                for dr, dc in directions:
                    r_next, c_next = r_rotten + dr, c_rotten + dc
                    if (0 <= r_next < m and
                        0 <= c_next < n and
                        grid[r_next][c_next] == 1 and
                        (r_next, c_next) not in visited
                    ):
                        n_fresh -= 1
                        queue.append((r_next, c_next))
                        visited.add((r_next, c_next))
            if queue:
                minute += 1
        return minute if not n_fresh else -1
