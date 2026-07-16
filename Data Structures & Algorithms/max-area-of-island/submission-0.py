class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # T: O(M * N) | S: O(M * N)
        # M = Size of grid rows
        # N = Size of grid columns
        visited = set()
        directions = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]
        max_area_island = 0
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 or (r, c) in visited:
                    continue
                area_island = 1
                stack = [(r, c)]
                visited.add((r, c))
                while stack:
                    r_island, c_island = stack.pop()
                    for dr, dc in directions:
                        r_next, c_next = r_island + dr, c_island + dc
                        if (0 <= r_next < m and
                            0 <= c_next < n and
                            grid[r_next][c_next] == 1 and
                            (r_next, c_next) not in visited
                        ):
                            area_island += 1
                            stack.append((r_next, c_next))
                            visited.add((r_next, c_next))
                max_area_island = max(max_area_island, area_island)
        return max_area_island
