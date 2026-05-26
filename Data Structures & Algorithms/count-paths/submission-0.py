class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # only down/right so if use recursion, r+1,c or r,c+1
        # unique path can be from final destination first bottom-top approach
        # rows: m, cols: n 

        # can ensure that you have 2 rows in memory at the same time
        # the right most column is all 1 cos like from the 2nd bottom if u can only go down so its like 
        # 1 way only

        # make dummy row of 0s below the actual grid 
        prev = [0] * n

        # start from bottom
        for r in range(m - 1, -1, -1):
            curr = [0] * n
            curr[-1] = 1 # set last column to be 1 

            # update from right to left cos if from left to right since movement is to the right,
            # value is not updated yet
            for c in range(n-2, -1, -1):
                curr[c] = prev[c] + curr[c+1]

            prev = curr

        return prev[0]
        
        