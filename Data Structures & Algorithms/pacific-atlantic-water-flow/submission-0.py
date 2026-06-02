class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # need to do recursion from (r+1, c), (r-1, c), (r,c+1), (r,c-1)
        # if you start in the middle u cant really go through all the cells
        # so u gotta go iterate through each cell
        # just keep a seen set so that if the cell that ur visiting is already 
        # in the set, you just continue

        # the goal is to get to any of the boundary cells 0, rows-1 or cols-1
        # defo need to divide between pacific and atlantic
        # the rules are that it can only move to neighboring cell with height
        # equal or lower

        # the cells need to achieve both corners 

        rows, cols = len(heights), len(heights[0])
        # run dfs only on edges, separate visited set for pacific and atlantic cells
        # so that you dont have to run from every single cell O(r*c)
        pacific, atlantic = set(), set()

        # keep track of previous height
        def dfs(r, c, visited, prevHeight):
            # base case, out of bounds or height more than previous height
            if (r == rows or c == cols or r < 0 or c < 0 or (r,c) in visited or heights[r][c] < prevHeight):
                return
            
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        # goal iterations
        # pacific c = 0, r = any or r = 0, c any 
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])

        # atlantic r = rows-1, c = any or c = cols-1, r=any 
        for r in range(rows):
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        for c in range(cols):
            dfs(rows-1, c, atlantic, heights[rows-1][c])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res 
    