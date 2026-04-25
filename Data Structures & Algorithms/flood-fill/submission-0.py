class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]

        def dfs(image, r, c, visit):
            ROWS, COLS = len(image), len(image[0])
            # base cases
            if r == ROWS or c == COLS or min(r,c) < 0 or image[r][c] != start_color or (r,c) in visit:
                return 
            if image[r][c] == start_color:
                image[r][c] = color

            visit.add((r, c))

            dfs(image, r+1, c, visit)
            dfs(image, r-1, c, visit)
            dfs(image, r, c+1, visit)
            dfs(image, r, c-1, visit)

        dfs(image, sr, sc, set())
        return image