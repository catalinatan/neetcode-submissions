from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # shortest path so bfs 
        # horizontal/vertical adjacent
        neighbors = [[0,1], [1,0], [-1, 0], [0,-1]] 

        # preamble
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0 

        # visit every cell 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1 # count how many fresh fruits there are to ensure theres none in the end
                elif grid[r][c] == 2:
                    queue.append((r,c)) # add the cells containing the rotten fruits to visit
        
        minutes = 0
        while queue and fresh > 0:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr == rows or nc < 0 or nc == cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
                    fresh -= 1
                
        # impossible state handling
        return minutes if fresh == 0 else -1