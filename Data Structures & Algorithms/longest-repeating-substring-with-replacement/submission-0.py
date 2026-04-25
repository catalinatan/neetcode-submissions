from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count[c] = frequency of each char in current window 
        # maxf = max. freq in the window 
        # no of replacements needed to make all chars the same is 
        # window_size - maxf
        count = defaultdict(int)
        l = 0 
        maxf = 0 
        res = 0 

        for r in range(len(s)):
            count[s[r]] += 1 
            maxf = max(maxf, count[s[r]])
            # window size = (r-l+1)

            # need more than k replacements, shrink window 
            while (r-l+1) - maxf > k:
                count[s[l]] -= 1 
                l += 1 

            res = max(res, r-l+1)
                
        return res 