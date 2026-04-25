class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR if 2 bits are the exact same they'll equal 0 e.g. 1 and 1 becomes 0, 0 and 0 becomes 0 
        res = 0 # n ^ (XOR) 0 = n whether n is 0 or 1 

        for n in nums:
            res = n ^ res
        return res



