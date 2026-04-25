class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # n = len(matrix) 

        # for r in range(n):
        #     for c in range(r+1, n): # diagonal when r=c stay the same after transpose
        #         matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            
        # for r in range(n):
        #     matrix[r].reverse()
       
        l, r = 0, len(matrix)-1

        while l < r:
            for i in range(r-l): # 3 rotations only
                top, bot = l, r # square matrix

                # save topleft
                topLeft = matrix[top][l+i]

                # move bottom left into topleft
                matrix[top][l+i] = matrix[bot - i][l]

                # move bottom right into bottom left
                matrix[bot - i][l] = matrix[bot][r - i]

                # move top right into bottom right
                matrix[bot][r -i] = matrix[top + i][r]

                # move top left into top right
                matrix[top +i][r] = topLeft 

            r -= 1 
            l += 1 


                