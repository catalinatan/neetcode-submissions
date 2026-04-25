class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0 
        # decision tree to either do 1 step or 2 steps at each of the steps
        # start at step 0 and we want to get n steps reached
        # once u find one path reached then add counter


        # time complexity would be O(2^n) where n is the depth and 2 is the 
        # max decisions in each node 

        # can store paths in memory so no need to run decision tree again 
        # but if u do pruning just its just O(n) since u resolve the sub-problem once
        # cache result use memoization 

        # start from the bottom and then work your way up 
        # bottom-up DP approach 

        # store result in DP from index 0 to n 
        # base case is last step theres only gonna be 1 

        # kind of like sliding window 
        one, two = 1, 1

        for i in range(n-1): 
            temp = one
            one = one + two # add 2 previous values and then get the result
            two = temp # shift the 2 
        
        return one