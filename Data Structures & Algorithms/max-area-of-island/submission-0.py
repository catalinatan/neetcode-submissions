class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r: int, c: int) -> int:
            # bounds
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            # water or already seen
            if grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))
            return (
                1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))

        return max_area


            
