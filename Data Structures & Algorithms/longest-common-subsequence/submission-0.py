class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # the choice is either to delete/ignore or move forward 
        # need to keep track of the length of the common letters
        # has to be in order 

        # brute force is to go through each letter in text2 then
        # check if the letter exists in text1
        # if the letter exists append to result
        # and keep track of max length
        # if suddenly keep track of letter thats in text1 but not in order then
        # make new substring and update max length
        # if reach the end of text2, return result 

        # if characters of string match, character is part of longest common subsequence, so 
        # add to remaining prefix

        # if not match then 2 choices: skip char from text1 or skip char from text2 
        # LCS is max of those 2 options

        
        # make an empty grid, bottom --> top approach 
        rows, cols = len(text1)+1, len(text2)+1 
        # create extra row/column so that for loop doesnt go out of range
        # if we are in the last row of row index m it means text1 has no characters left, so LCS with
        # any suffix of text2 is always 0

        # col idx (last column) represents text2 having no chars left
        grid = [[0] * cols for r in range(rows)]

        # start from bottom right corner, from right to left
        for r in range(rows-2, -1, -1):
            for c in range(cols-2,-1,-1):
                if text1[r] == text2[c]:
                    # move diagonally if match
                    grid[r][c] = 1 + grid[r+1][c+1]
                else:
                    # if move right c+1 that means ur skipping char from text2, 
                    # if move down r+1 that means ur skipping char from text1
                    grid[r][c] = max(grid[r][c+1], grid[r+1][c])
        
        return grid[0][0]