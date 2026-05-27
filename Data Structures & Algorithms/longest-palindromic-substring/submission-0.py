class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force solution: 
        # make a permutation combination of all subsequences 
        # individually check if they are valid palindromes using 2 pointers
        # time complexity is O(n^3), O(n^2) substrings and each check takes O(n) with 2 pointers
        
        # better approach is to expand around the center
        # treat each char and each gap as teh center of a palindrome then expand outward 

        # time complexity is O(n62) and O(1) space

        def expand(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]: # valid palindrome
                l -= 1 
                r += 1 
            # if l or r is out of bounds, exit while loop then restore to previous index
            # that is in bounds thats why we return l + 1 and r - 1 
            return l + 1, r - 1

        # handle cases for both odd and even length substrings
        res = ""
        res_len = 0
        
        for i in range(len(s)):
            # odd expansion (center at i)
            l, r = expand(i, i)
            if r-l+1 > res_len:
                res = s[l:r+1]
                res_len = r-l+1
            
            # even expansion (center between i and i+1)
            if i+1 < len(s):
                l, r = expand(i, i+1)
                if r-l+1 > res_len:
                    res = s[l:r+1]
                    res_len = r-l+1
        
        return res