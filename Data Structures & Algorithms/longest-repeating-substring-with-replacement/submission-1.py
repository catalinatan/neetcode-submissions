from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # probably best if u take the most frequent letter in the string and then like
        # but if use dict for frequency then u need to sort it each time which is not efficient
        # count how many letters are not that mode letter 
        # then return the length of the string either after k replacements or no of letters
        # thats not the mode letter cos 
        # or maybe just count how many replacements uve done so far in the window
        # if no of replacements exceed k then 

        # keep track of letter frequency with dict
        chr_count = Counter()
        l, r = 0, 0 
        maxw, maxf = 0, 0 

        while l <= r and r <= len(s)-1: 
            chr_count[s[r]] += 1 
            # update max frequency (mode)
            maxf = max(maxf, chr_count[s[r]])
            # window length
            length = r - l + 1
            
            # shrink window from the left
            # check if valid window
            if length - maxf > k:
                chr_count[s[l]] -= 1 
                l += 1
                length -= 1 # update length of window
            
            # window is valid then calc max length
            maxw = max(maxw, length)
            r += 1
        return maxw