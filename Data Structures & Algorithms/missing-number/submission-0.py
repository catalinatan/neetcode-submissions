class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # can convert all numbers to binary and like 
        # binary numbers the way you increase is like shift to the left
        # then add 1 

        # like 001 010 011 etc
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual
        
        