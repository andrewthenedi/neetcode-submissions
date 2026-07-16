class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # T: O(M * N) | S: O(M * N)
        # M = Size of grid rows
        # N = Size of grid columns
        visited = set()
        num_islands = 0
        positions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "0" or (r, c) in visited:
                    continue
                stack = [(r, c)]
                visited.add((r, c))
                while stack:
                    r_island, c_island = stack.pop()
                    for r_pos, c_pos in positions:
                        r_next, c_next = r_island + r_pos, c_island + c_pos
                        is_within_bounds = (0 <= r_next <= m - 1) and (0 <= c_next <= n - 1)
                        if is_within_bounds \
                            and grid[r_next][c_next] == "1" \
                            and (r_next, c_next) not in visited:
                            stack.append((r_next, c_next))
                            visited.add((r_next, c_next))
                num_islands += 1
        return num_islands
