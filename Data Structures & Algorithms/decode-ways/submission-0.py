class Solution:
    def numDecodings(self, s: str) -> int:
        # if 0 needs to be coupled with the bumber before if less than 26, 
        # else has to be alone

        # brute force would be to try to iterate O(s^2) times to see the different combinations
        # limit is 32 bit integer

        # when u iterate through the string the choice is either to join with the next one or 
        # stay on ur own 
        
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1

        # number of ways to decode the substring starting at index i s[i:], the answer is dp[0]
        for i in range(n-1, -1, -1):
            # this is the start of the range so if it starts with 0 
            # then its a leading zero and cannot be grouped with anything else
            if s[i] == "0":
                dp[i] = 0 
            else:
                # take one digit, the rest of the string is s[i+1:] so you add dp[i+1] into the solution
                dp[i] += dp[i+1]

                # take 2 digits if it exists, then the rest of the string is s[i+2:] so you add it to dp[i]
                # remember s[i:i+2] excludes i+2
                if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                    dp[i] += dp[i+2]


        return dp[0]


        