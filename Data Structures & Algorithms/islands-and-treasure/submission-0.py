import math
from collections import deque 

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2**31 - 1
        q = deque()

        # start BFS from all treasures (0)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()

            neighbors = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]

            for nr, nc in neighbors:
                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue
                if grid[nr][nc] != INF:   # skip walls (-1) and already-set distances and treasures
                    continue

                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))
            
                        


           
