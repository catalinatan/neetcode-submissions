class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        max_length = 0 
        l, r = 0, 0 
        seen = set()

        while l <= r and r < len(s): 
            if s[r] not in seen:
                seen.add(s[r])
                max_length = max(max_length, r - l + 1)
                r += 1
            else: # if we do l = r here its not a sliding window anymore its compartments
                seen.remove(s[l]) # shrink window from the left until theres no duplicates
                l += 1

        return max_length