class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 pointers
        l, r = 0, len(s)-1

        # case-insensitive so use lowercase 
        # need to make sure its alphanumeric so .isalnum

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            l_word = s[l].lower()
            r_word = s[r].lower()

            if l_word != r_word:
                return False

            l += 1 
            r -= 1 

        return True