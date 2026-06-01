class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # can convert all numbers to binary and like 
        # binary numbers the way you increase is like shift to the left
        # then add 1 

        # like 001 010 011 etc
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res
        # n = len(nums)
        # expected = n * (n + 1) // 2
        # actual = sum(nums)
        # return expected - actual
        
        