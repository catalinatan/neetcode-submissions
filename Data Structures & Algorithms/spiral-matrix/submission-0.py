class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        res = []

        l, r = 0, cols - 1
        top, bot = 0, rows - 1

        while top <= bot and l <= r:
            # 1) top row
            for c in range(l, r + 1):
                res.append(matrix[top][c])
            top += 1

            # 2) right column
            for row in range(top, bot + 1):
                res.append(matrix[row][r])
            r -= 1

            # 3) bottom row (only if still valid rows)
            if top <= bot:
                for c in range(r, l - 1, -1):
                    res.append(matrix[bot][c])
                bot -= 1

            # 4) left column (only if still valid cols)
            if l <= r:
                for row in range(bot, top - 1, -1):
                    res.append(matrix[row][l])
                l += 1

        return res
