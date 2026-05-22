class Solution:
    def climbStairs(self, n: int) -> int:
        # decision tree kind of like fibonacci but you can either
        # walk 1 or 2 and if u start from 0 
        # ull use the bottom top approach where u either choose to go
        # 1 or 2 

        # or u do top down approach from n  

        # top down approach
        # ans = n - 1
        # or ans = n-2 then recursively check 
        # for each path its either -1 or -2 again
        # if it reaches 0 base case then return 1 cos that means 1 path exist
        # else keep going

        ### brute force approach
        # if n <= 1:
        #     return 1

        # # return the sum of the 2 combinations
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # bottom up approach 
        # exactly like fibonacci where ways(i) = ways(i-1) + ways(i-2)
        # since u can either step 1 step or 2 step backwards
        if n <= 2: 
            return n 
        prev2, prev1 = 1, 2 # base case is either 1 or 2 
        for i in range(3, n+1):
            curr = prev1 + prev2
            prev2, prev1 = prev1, curr
        return prev1

