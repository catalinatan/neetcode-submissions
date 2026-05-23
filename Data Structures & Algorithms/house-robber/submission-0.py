class Solution:
    def rob(self, nums: List[int]) -> int:
        # kind of have to look at 3 elements at a time and like chooose the max one then like kind of see the window
        # that starts from like the max +2 onwards

        # maybe keep track of indices in a growing window so like cannot be i + 1 of each other
        
        # 2 possibilities :
        # 1) rob this house that means you havent rob the previous house so total is nums[i] + best up to house i-2
        # 2) skip this house so take up to best previous house (i-1)

        # at each step you choose max of this too so
        prev2, prev1 = 0, 0 

        # prev2 best money up to house i-2
        # prev1 best money up to house i-1
        new_best = 0 
        # maybe can use some sort of sum like keep track of the last sum and current value
        for i in range(0, len(nums)):
            new_best = max(nums[i] + prev2, prev1)
            prev2, prev1 = prev1, new_best
        return new_best