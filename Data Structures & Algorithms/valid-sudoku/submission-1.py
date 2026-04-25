class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])

        if row != 9 or col != 9:
            return False

        for row in board:
            num_list = []
            for num in row: 
                if num.isnumeric():
                    num_list.append(num)
                
            num_set = set(num_list)
            if len(num_set) != len(num_list):
                return False
        
        for col in range(9):
            num_list = []
            for row in range(9):
                num = board[row][col] 
                if num != "." and not num.isnumeric():
                    return False 
                if num.isnumeric():
                    num_list.append(num)
            num_set = set(num_list)
            if len(num_set) != len(num_list):
                return False

        for i in range(0, row-3, 3):
            for j in range(0, row-3, 3):
                num_list = []
                for r in range(i, i+3): 
                    for c in range(j, j+3): 
                        num = board[r][c]
                        if num.isnumeric():
                            num_list.append(num)
                num_set = set(num_list)
                if len(num_set) != len(num_list):
                    return False
        return True


