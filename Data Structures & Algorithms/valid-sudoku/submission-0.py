class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check if numbers in the same column are duplicates
        check_col_list = [[row[col] for row in board] for col in range(9)]

        for col in check_col_list: 
            if len([num for num in col if num != '.']) != len({num for num in col if num != '.'}):
                return False

        # Check if numbers in the same row are duplicates
        for row in board:
            if len([x for x in row if x != '.']) != len({x for x in row if x != '.'}):
                return False
  
        # starting row index = block_row * 3 
        # starting column index = block_column * 3 
        for block_row in range(3): 
            for block_col in range(3):
                block_list = [board[i][j] for j in range(block_col * 3, block_col * 3 + 3) for i in range(block_row * 3, block_row * 3 + 3)]
                if len([elmnt for elmnt in block_list if elmnt != "."]) != len({elmnt for elmnt in block_list if elmnt != "."}):
                    return False

        return True


