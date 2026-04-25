class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        for r in range(row):
            if matrix[r][0] <= target <= matrix[r][col-1]: 
                for c in range(col):
                    if matrix[r][c] == target:
                        return True
        return False