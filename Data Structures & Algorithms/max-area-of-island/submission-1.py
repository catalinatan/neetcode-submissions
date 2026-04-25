class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            # base case
            if r == rows or c == cols or (r,c) in visit or min(r,c) < 0 or grid[r][c] == 0:
                return
            
            self.count += 1 
            visit.add((r,c))

            # recursion
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                # new island
                if grid[r][c] == 1 and (r,c) not in visit:
                    self.count = 0 
                    dfs(r,c)
                    max_area = max(max_area, self.count)
        
        return max_area