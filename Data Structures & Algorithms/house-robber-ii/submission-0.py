class Solution:
    def rob(self, nums: List[int]) -> int:
        # add extra condition where 0 and len(nums) are neighbors
        # which means u have 2 scenarios: either include the first house, or include the last house
        # cannot do both, need to maximise both scenarios

        # start from original house robbers first before expanding to house robber II

       
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self,nums):
        prev2, prev1 = 0, 0 
        best_sum = 0 

        for i in range(len(nums)):
            best_sum = max(nums[i] + prev2, prev1)
            prev1, prev2 = best_sum, prev1

        return prev1

