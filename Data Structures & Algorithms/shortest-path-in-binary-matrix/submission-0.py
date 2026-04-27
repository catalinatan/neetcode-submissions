from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = {(0, 0)}
        q = deque([(0, 0)])
        length = 1

        if grid[0][0] == 1:
            return -1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                # reach the end
                if r == rows - 1 and c == cols - 1:
                    return length
                
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, 1], [-1, -1], [1, -1], [1, 1]]
                for dr, dc in neighbors:
                    if min(r+dr,c+dc) < 0 or r+dr == rows or c+dc == cols or grid[r+dr][c+dc] == 1 or (r+dr,c+dc) in visit:
                        continue
                    q.append((r+dr,c+dc))
                    visit.add((r+dr,c+dc))
            length += 1

        return -1