class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # need count to keep track of islands
        # islands need to be all val 1 and adjacent to each other 

        self.count = 0 
        rows, cols = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r,c, visit):
            # Base Case
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visit or grid[r][c] == "0":
                return

            # Note visited cells
            visit.add((r,c))

            dfs(r+1, c, visit)
            dfs(r-1, c, visit)
            dfs(r, c+1, visit)
            dfs(r, c-1, visit)
            
        for r in range(0,rows):
            for c in range(0,cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    self.count += 1
                    dfs(r,c,visit)
        return self.count