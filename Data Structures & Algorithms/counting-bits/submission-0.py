class Solution:
    def countBits(self, n: int) -> List[int]:
        # brute force approach is to do a for loop until n 
        # check how many divisible by 2 
        # bits in which place is 2^n 
        # if divisible by 2 that means its just 1 single bit,
        # if theres remainder gotta like keep dividing by multiples of 2
        # like while divide 

        # res = [0] * (n+1)
        # # brute force: 
        # def count_bit_ones(x):
        #     count = 0 
        #     while x > 0:
        #         # if can divide by 2, that means its a single bit 
        #         if x % 2 == 1:
        #             count += 1 
        #         x //= 2 # shift right basically divide by 2
        #     return count

        # for i in range(n+1):
        #     res[i] = count_bit_ones(i)
        
        # return res

        # any number i = highestPowerOfTwo (e.g. 2,4,8) + remainder
        # 13 = 8 + 5
        # binary representation of a number is 
        # the leading 1 from the biggest power of two 
        # plus the binary pattern of the remainder
        # 1 (for the highest power of two) + number of set bits in the remainder

        dp = [0] * (n+1)
        offset = 1 
        
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i 
            dp[i] = 1 + dp[i-offset]
        return dp
